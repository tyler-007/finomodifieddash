import pandas as pd
import numpy as np
import openai
import matplotlib.pyplot as plt
import random
from config import organisation as organization_name

def get_completion(prompt, model="gpt-4-turbo", temperature=0):
      
    messages = [
        {"role": "system", "content": f"You are a kind business insight employee with speciality in online media sentiment analysis, you work in  an organization - {organization_name} provided by the user."},
        {"role": "assistant", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
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
    openai.api_key=api_key
    data = data.sample(n=random.randint(500, 999), random_state=42)
    dict_obt = labelling(data)
    list_response = []

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


