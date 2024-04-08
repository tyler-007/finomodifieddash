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

        df = process_csv_file(uploaded_file)

        '''st.subheader("Dashboard for all applications")
        sentiment_fig, facebook_fig, instagram_fig, twitter_fig, youtube_fig, linkedin_fig = generate_dashboard(df)

        # Create a 3x3 grid layout
        row1 = st.columns(3)
        row2 = st.columns(3)

        # Place charts in the grid
        for col, fig, header in zip(row1 + row2, [sentiment_fig,twitter_fig, facebook_fig, instagram_fig, linkedin_fig, youtube_fig], ["Cummulative","Twitter", "Facebook", "Instagram", "LinkedIn", "YouTube"]):
            with col:
                st.header(header)
                st.image(fig)'''
        


        '''st.subheader("WordCloud for all applications")
        content_fig_Wc, facebook_fig_Wc, instagram_fig_Wc, twitter_fig_Wc, youtube_fig_Wc, linkedin_fig_Wc = generate_word_cloud(df)

        # Create a 3x3 grid layout
        row1 = st.columns(3)
        row2 = st.columns(3)

        # Place charts in the grid
        for col, fig, header in zip(row1 + row2, [content_fig_Wc,twitter_fig_Wc, facebook_fig_Wc, instagram_fig_Wc, linkedin_fig_Wc, youtube_fig_Wc], ["Cummulative","Twitter", "Facebook", "Instagram", "LinkedIn", "YouTube"]):
            with col:
                st.header(header)
                st.image(fig)'''

        # Generate Suggestions

        st.subheader("AI Suggestions")
        suggestions = generate_suggestions(api_key, df)
        for suggestion in suggestions:
            st.text(suggestion)

       
if __name__ == "__main__":
    main()
