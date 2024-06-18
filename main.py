from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import subprocess

load_dotenv()  # Loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")

# def get_gemini_response(question):
# response = model.generate_content(question)
# return response.text


# Initialize our Streamlit app
st.set_page_config(page_title="ScriptInkVisualizer")

st.header("ScriptInkVisualizer")

# Input textbox
# input_text = st.text_input("Input: ", key="input")

# Add image at the center of the page
#with st.container():
#    st.write("add a image here")

# Layout for buttons in the same line
col1, col2, col3 = st.columns(3)

# Button 1
submit_button_1 = col1.button("ChatBot")

# Button 2
submit_button_2 = col2.button("Image captioning")

# Button 3
submit_button_3 = col3.button("PDF")

# When any button is clicked
if submit_button_1 or submit_button_2 or submit_button_3:
    if submit_button_1:
        st.subheader("Running ChatBot...")
        # Execute the command in the terminal
        command = "streamlit run ChatBot.py"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Display the output and error in Streamlit
        st.text("Output:")
        st.text(output.decode())

        st.text("Error:")
        st.text(error.decode())
    elif submit_button_2:
        st.subheader("Running Image Captioning...")
        # Execute the command in the terminal
        command = "streamlit run ImageCaption.py"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Display the output and error in Streamlit
        st.text("Output:")
        st.text(output.decode())

        st.text("Error:")
        st.text(error.decode())
    elif submit_button_3:
        st.subheader("Running PDF...")
        # Execute the command in the terminal
        command = "streamlit run vision.py"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Display the output and error in Streamlit
        st.text("Output:")
        st.text(output.decode())

        st.text("Error:")
        st.text(error.decode())

        # if input_text != "":
        '''response = get_gemini_response(input_text)
        st.subheader("Response is")
        st.write(response)'''
    # else:
    #   response = "invalid input"
    #  st.write(response)
