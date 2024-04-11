import pandas as pd
import numpy as np
import openai
import matplotlib.pyplot as plt
import random
from config import organisation as organization_name

# Upgrade OpenAI library to the latest version

# Use the most powerful available model with optimized parameters
model = "text-davinci-003"  # Currently the most powerful model as of Apr 11, 2024
temperature = 0.5  # Balance creativity and coherence
max_tokens = 150  # Limit output length for conciseness

def get_completion(prompt):
    messages = [
        {"role": "system", "content": f"You are a kind business insight employee with speciality in online media sentiment analysis, you work in an organization - {organization_name} provided by the user."},
        {"role": "assistant", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=None  # Prevent premature truncation
    )

    return response.choices[0].message["content"]

list_response = []

def labelling(data):
    sentiment_content_dict = {}
    for index, row in data.iterrows():
        sentiment = row['Sentiment']
        content = row['Content']
        if sentiment in sentiment_content_dict:
            sentiment_content_dict[sentiment].append(content)
        else:
            sentiment_content_dict[sentiment] = [content]
    return sentiment_content_dict

def generate_suggestions(api_key, data):
    random_number = random.randint(500, 999)
    data = data.sample(n=random_number, random_state=42)
    openai.api_key = api_key
    dict_obt = labelling(data)

    for sentiment in dict_obt.keys():
        prompt = f""" 
As a business insights expert at {organization_name}, you have been tasked with analyzing the {sentiment} feedback received from various social media platforms where {organization_name} is active. The dataset contains comments categorized as {sentiment}.\

Your objective is to thoroughly analyze the {sentiment} feedback by reading, memorizing, and interpreting all comments in this category. After analysis, you are required to present the top 5 insights derived from the sentiment. These insights should reflect the prevailing sentiment of the people and provide a deeper understanding of their feelings.\

Furthermore, for each insight, you must provide a percentage stat indicating the proportion of comments expressing the same sentiment out of the total comments analyzed. For example, "35% of the total positive comments expressed satisfaction with the user interface (UI)."\

The top 5 insights will be compiled as bullet points and presented to the Directors of the company for review and action.\

Please ensure that your analysis is concise and focuses on the most significant findings. Limit your output to only 5 bullet points, each accompanied by its respective percentage stat.\

"""
        response = get_completion(prompt)
        list_response.append(response)
    return list_response

# Example usage:
# api_key = "your_openai_api_key_here"
# data = pd.read_csv("path_to_your_dataset.csv")
# organization_name = "User Input Organization"
# suggestions = generate_suggestions(api_key, data, organization_name)
# print(suggestions)
