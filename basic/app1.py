import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Interactive Metabolic Risk Dashboard & Calculator")

def uploaded_file():
    try:
        df = pd.read_csv("diabetes_risk_prediction_dataset-selected-columns.csv")
        return df
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

data = uploaded_file()

if data is not None:
    df = data

    # 🎨 Page setup
    st.set_page_config(page_title="Your Health, Your Journey", layout="wide")

    # 🌟 Title
    st.markdown("<h1 style='text-align:center; color:#0078D7;'>Your Health, Your Journey</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:red;'>Explore, Learn & Thrive!</h3>", unsafe_allow_html=True)
    st.write("---")

    # 🧠 Interactive Flipcards Grid
    st.subheader("💡 Interactive Health Flipcards")

    cols = st.columns(3)

    with cols[0]:
        st.markdown("### 🍎 Nutrition")
        with st.expander("Tap to Flip"):
            st.info("Eating more fruits and vegetables daily lowers your risk of chronic diseases.")

    with cols[1]:
        st.markdown("### 🏃 Exercise")
        with st.expander("Tap to Flip"):
            st.info("Just 30 minutes of brisk walking can improve cardiovascular health and reduce stress.")

    with cols[2]:
        st.markdown("### 😴 Sleep")
        with st.expander("Tap to Flip"):
            st.info("Regular sleep of 7–8 hours improves insulin sensitivity and boosts memory.")

    # ✨ Motivational Quote
    st.write("---")
    st.markdown(
        "<div style='text-align:center; font-size:20px; color:#FF5733;'>💬 Small steps lead to big changes. Start today!</div>",
        unsafe_allow_html=True,
    )

    # 🏃 Lifestyle Collage Section
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=100)
        st.caption("🍎 Healthy Eating")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1046/1046786.png", width=100)
        st.caption("🏃 Active Living")
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/1046/1046792.png", width=100)
        st.caption("😴 Rest & Recovery")

    # ✨ Motivational Quote
    st.write("---")
    st.markdown(
        "<div style='text-align:center; font-size:20px; color:#FF5733;'>"
        "💬 Small steps lead to big changes. Start today!"
        "</div>",unsafe_allow_html=True
    )
    #Preprocessing ---
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

    # --- Sidebar Navigation ---
    section = st.sidebar.radio("Choose Section", ["Global Dashboard", "Personal Calculator"])

    # --- Section 1: Global Dashboard ---
    if section == "Global Dashboard":
        st.header("📊 Global Population Dashboard")

        # Tier Distribution
        st.subheader("Tier Distribution Table")
        st.table(tier_counts)

        st.subheader("Tier Distribution Chart")
        fig1 = px.bar(tier_counts, x="Risk_Tier", y="Count", color="Risk_Tier",
                      title="Tier Distribution")
        st.plotly_chart(fig1)

        # Average Age
        st.subheader("Average Age per Tier")
        st.table(avg_age)

        fig2 = px.bar(avg_age, x="Risk_Tier", y="Average_Age", color="Risk_Tier",
                      title="Average Age per Tier")
        st.plotly_chart(fig2)

        # Blood Glucose Distribution
        st.subheader("Blood Glucose Distribution by Tier")
        fig3 = px.box(df, x="Risk_Tier", y="Blood_Glucose", color="Risk_Tier",
                      title="Blood Glucose Distribution")
        st.plotly_chart(fig3)

        # BMI Distribution
        st.subheader("BMI Distribution by Tier")
        fig4 = px.box(df, x="Risk_Tier", y="BMI", color="Risk_Tier",
                      title="BMI Distribution")
        st.plotly_chart(fig4)

        # --- New Visualizations ---
        # Pie Chart
        st.subheader("BMI Risk Tier Distribution (Pie Chart)")
        fig_pie = px.pie(tier_counts, names="Risk_Tier", values="Count",
                         title="Percentage of Population in Each Risk Tier")
        st.plotly_chart(fig_pie)

        # Box Plot with Outliers
        st.subheader("BMI Spread by Risk Tier (Box Plot)")
        fig_box = px.box(df, x="Risk_Tier", y="BMI", color="Risk_Tier",
                         title="BMI Distribution Across Risk Tiers",
                         points="all")
        st.plotly_chart(fig_box)

        # Obesity Chart by Country
        st.subheader("Obesity Categories by Country")

        def bmi_category(bmi):
            if bmi < 25:
                return "Normal"
            elif bmi < 30:
                return "Increased Risk"
            else:
                return "High Risk"

        df["BMI_Category"] = df["BMI"].apply(bmi_category)

        if "Country" in df.columns:
            country_counts = df.groupby(["Country", "BMI_Category"]).size().reset_index(name="Count")

            fig_obesity = px.bar(country_counts, x="Country", y="Count", color="BMI_Category",
                                 barmode="group", title="Obesity Categories by Country")
            st.plotly_chart(fig_obesity)
        else:
            st.warning("Dataset has no 'Country' column. Please add one to view obesity chart.")

    # --- Section 2: Personal Calculator ---
    elif section == "Personal Calculator":
        st.header("🧮 Personal Risk Assessment Calculator")

        # Input form
        age = st.number_input("Age", min_value=1, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        waist = st.number_input("Waist Circumference (cm)", min_value=40, max_value=200, value=85)
        glucose = st.number_input("Blood Glucose (mg/dL)", min_value=50, max_value=300, value=100)
        hba1c = st.number_input("HbA1c (%)", min_value=3.0, max_value=15.0, value=5.5)

        if st.button("Calculate Risk"):
            bmi = weight / ((height/100) ** 2)

            if hba1c >= 6.5 or glucose >= 140 or bmi >= 30:
                tier = "High Risk"
            elif (hba1c >= 5.7 or glucose >= 100 or bmi >= 25):
                tier = "Moderate Risk"
            else:
                tier = "Low Risk"

            bmi_percentile = (df["BMI"] < bmi).mean() * 100

            st.success(f"Your BMI is {bmi:.2f}.")
            st.info(f"You fall into the **{tier}** category.")
            st.write(f"Your BMI is higher than {bmi_percentile:.1f}% of the population.")

            st.subheader("Lifestyle Suggestions")
            if tier == "High Risk":
                st.write("- Consult a healthcare provider.")
                st.write("- Reduce sugar intake.")
                st.write("- Increase daily physical activity.")
            elif tier == "Moderate Risk":
                st.write("- Monitor vitals regularly.")
                st.write("- Maintain consistent sleep/exercise.")
                st.write("- Focus on portion control.")
            else:
                st.write("- Continue healthy habits.")
                st.write("- Stay active.")
                st.write("- Regular preventive checkups.")
else:
    st.warning("Please upload the dataset to proceed.")
