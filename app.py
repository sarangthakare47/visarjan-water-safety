import streamlit as st
import pandas as pd
import joblib

model=joblib.load("visarjan_model.pkl")

df = pd.read_csv("maharashtra_water_quality.csv")

st.title("Water Safety for Ganpati Visarjan")
st.subheader("Check if the Water Body in your City is safe for Visarjan")

city = st.selectbox("Select City", sorted(df["City"].unique()))
st.success("You selected a city")

waterbodies=df[df["City"]==city]["Waterbody"].unique()
waterbody = st.selectbox("Select Waterbody", waterbodies)
st.success(" You selected a Waterbody")

row = df[(df["City"] == city) & (df["Waterbody"] == waterbody)].iloc[0]

st.subheader("Water Quality Parameters")
col1, col2 = st.columns(2)
with col1:
    st.write(f"**pH:** {row['pH']}")
    st.write(f"**DO:** {row['DO']}")
    st.write(f"**BOD:** {row['BOD']}")
with col2:
    st.write(f"**Turbidity:** {row['Turbidity']}")
    st.write(f"**TDS:** {row['TDS']}")

X = [[row["pH"], row["DO"], row["BOD"], row["Turbidity"], row["TDS"]]]


if st.button("Predict Safety"):
    pred = model.predict(X)[0]

    st.subheader("✅ Safety Results are")
    if pred == "Yes":
        st.success("This waterbody is SAFE for Visarjan 🌿")
    else:
        st.error("This waterbody is NOT SAFE for Visarjan ❌")

