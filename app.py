# Generating a script to upload a file and use perform comment analysis on the same file
import streamlit as st
from data_processing import process_csv_file
from ai_interaction import generate_suggestions
import pandas as pd
import config

def main():
    st.title("Fino Payments Bank Marketing Tool by Aayush Jain")
    config.organisation = st.text_input("Enter your Orgs Name")


    # File Upload
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    if uploaded_file is not None:
        # API Key Input
        api_key = st.text_input("Enter your API key")
        config.api_key=api_key

        df = process_csv_file(uploaded_file)

        st.subheader("AI Suggestions")
        suggestions = generate_suggestions(api_key, df)
        for suggestion in suggestions:
            st.text(suggestion)

       
if __name__ == "__main__":
    main()
