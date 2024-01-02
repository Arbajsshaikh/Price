# app.py
import streamlit as st
import pandas as pd

st.title("Excel Viewer App")

# Upload Excel file
uploaded_file = st.file_uploader("FINAL_REQUIREMENT.xlsx", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read Excel file
    df = pd.read_excel(uploaded_file, sheet_name="Sheet1")

    # Display DataFrame
    st.write("Excel File Contents:")
    st.dataframe(df)
