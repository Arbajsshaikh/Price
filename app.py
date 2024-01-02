import streamlit as st
import pandas as pd

# Load the data
sorted_df = pd.read_excel(r"FINAL_REQUIREMENT.xlsx")

# Display the DataFrame
st.dataframe(sorted_df)
