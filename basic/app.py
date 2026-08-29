import pandas as pd
import streamlit as st
import plotly.express as px

# --- Load dataset ---
df = pd.read_csv("diabetes_risk_prediction_dataset-selected-columns.csv")

# --- Data Preprocessing ---
for col in ["Height_cm", "Weight_kg", "Blood_Glucose", "HbA1c"]:
    df[col] = df[col].fillna(df[col].median())

# --- Feature Engineering ---
df["BMI"] = df["Weight_kg"] / ((df["Height_cm"]/100) ** 2)

# --- Risk Tier Segmentation ---
def assign_tier(row):
    if row["HbA1c"] >= 6.5 or row["Blood_Glucose"] >= 140 or row["BMI"] >= 30:
        return "High Risk"
    elif (row["HbA1c"] >= 5.7 or row["Blood_Glucose"] >= 100 or row["BMI"] >= 25):
        return "Moderate Risk"
    else:
        return "Low Risk"

df["Risk_Tier"] = df.apply(assign_tier, axis=1)

# --- Tables ---
tier_counts = df["Risk_Tier"].value_counts().reset_index()
tier_counts.columns = ["Risk_Tier", "Count"]

avg_age = df.groupby("Risk_Tier")["Age"].mean().reset_index()
avg_age.columns = ["Risk_Tier", "Average_Age"]

bg_distribution = df.groupby("Risk_Tier")["Blood_Glucose"].describe().reset_index()
bmi_distribution = df.groupby("Risk_Tier")["BMI"].describe().reset_index()

# --- Streamlit UI ---
st.title("Metabolic Risk Cohort Dashboard")

# Layout: Tables and Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tier Distribution Table")
    st.table(tier_counts)

    st.subheader("Average Age per Tier")
    st.table(avg_age)

with col2:
    st.subheader("Tier Distribution Chart")
    fig1 = px.bar(tier_counts, x="Risk_Tier", y="Count", color="Risk_Tier",
                  title="Tier Distribution")
    st.plotly_chart(fig1)

    st.subheader("Average Age Chart")
    fig2 = px.bar(avg_age, x="Risk_Tier", y="Average_Age", color="Risk_Tier",
                  title="Average Age per Tier")
    st.plotly_chart(fig2)

# Distribution plots
st.subheader("Blood Glucose Distribution by Tier")
fig3 = px.box(df, x="Risk_Tier", y="Blood_Glucose", color="Risk_Tier",
              title="Blood Glucose Distribution")
st.plotly_chart(fig3)

st.subheader("BMI Distribution by Tier")
fig4 = px.box(df, x="Risk_Tier", y="BMI", color="Risk_Tier",
              title="BMI Distribution")
st.plotly_chart(fig4)

# Executive Summary
st.subheader("Executive Summary")
st.write("""
- High Risk group shows elevated HbA1c, Blood Glucose, and BMI.
- Moderate Risk group trends toward overweight and pre-diabetic ranges.
- Low Risk group maintains healthier averages.
""")
