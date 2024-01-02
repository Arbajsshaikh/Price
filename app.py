# app.py
import streamlit as st
import pandas as pd

st.title("Excel Viewer App")

# Upload Excel file
uploaded_file = st.file_uploader("JUNE.csv", type=["csv"])

if uploaded_file is not None:
    # Read Excel file
    df = pd.read_csv(uploaded_file)

    # Display DataFrame
    st.write("Excel File Contents:")
    st.dataframe(df)
