import pandas as pd
import streamlit as st
import plotly.express as px

# --- Load dataset ---
df = pd.read_csv("diabetes_risk_prediction_dataset-selected-columns.csv")

# --- Tables ---
tier_counts = df["Risk_Tier"].value_counts().reset_index()
tier_counts.columns = ["Risk_Tier", "Count"]

st.subheader("BMI Risk Tier Distribution (Pie Chart)")
fig_pie = px.pie(tier_counts, names="Risk_Tier", values="Count",
                 title="Percentage of Population in Each Risk Tier")
st.plotly_chart(fig_pie)

st.subheader("BMI Spread by Risk Tier (Box Plot)")
fig_box = px.box(df, x="Risk_Tier", y="BMI", color="Risk_Tier",
                 title="BMI Distribution Across Risk Tiers",
                 points="all")  # shows outliers
st.plotly_chart(fig_box)

st.subheader("Obesity Categories by Country")

# Categorize BMI
def bmi_category(bmi):
    if bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Increased Risk"
    else:
        return "High Risk"

df["BMI_Category"] = df["BMI"].apply(bmi_category)

# Group by Country + BMI Category
country_counts = df.groupby(["Country", "BMI_Category"]).size().reset_index(name="Count")

fig_obesity = px.bar(country_counts, x="Country", y="Count", color="BMI_Category",
                     barmode="group", title="Obesity Categories by Country")
st.plotly_chart(fig_obesity)
