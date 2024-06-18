from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from datetime import datetime, timedelta
import re

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")


# Helper function to parse date queries
def parse_date_query(question):
    date_yesterday_pattern = re.compile(r'\b(yesterday|today|tomorrow)\b', re.IGNORECASE)
    date_specific_pattern = re.compile(r'\b(\d{4}-\d{2}-\d{2})\b')

    match_yesterday = date_yesterday_pattern.search(question)
    match_specific = date_specific_pattern.search(question)

    if match_yesterday:
        return match_yesterday.group(0).lower()
    elif match_specific:
        return match_specific.group(0)
    return None


def get_gemini_response(question):
    # Check if the question contains any date-related query
    date_query = parse_date_query(question)
    if date_query:
        # Handle date-related queries
        if date_query == "today":
            response = datetime.now().strftime("%Y-%m-%d")
        elif date_query == "yesterday":
            response = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        elif date_query == "tomorrow":
            response = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            response = date_query  # Return the specific date if provided
    else:
        # Use Gemini model to generate response
        response = model.generate_content(question).text

    return response


# Initialize our Streamlit app
st.set_page_config(page_title="ScriptInkVisualizer Demo")
st.header("ScriptInkVisualizer")

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# When submit button is clicked
if submit_button:
    response_text = get_gemini_response(input_text)
    st.subheader("Response is")
    st.write(response_text)
