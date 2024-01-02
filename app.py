import streamlit as st
import pandas as pd

# Load the data
sorted_df = pd.read_excel(r"D:\data\SALIM_SIR\FINAL_REQUIREMENT.xlsx")

# Display the DataFrame
st.dataframe(sorted_df)
