from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import subprocess

load_dotenv()  ##loading all the environment variables
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load Gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


##initialize our streamlit app
st.set_page_config(page_title="ScriptInkVisualizer Demo")
st.header("ScriptInkVisualizer")

input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to run streamlit app.py
#'''if st.button("Chatbot"):
#    st.write("not yet implemented")
#     st.subheader("Running chatbot...")
#     # Execute the command in the terminal
#     command = "streamlit run main.py"
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, error = process.communicate()
#
#     # Display the output and error in Streamlit
#     st.text("Output:")
#     st.text(output.decode())
#
#     st.text("Error:")
#     st.text(error.decode())'''

# Button to submit and get Gemini response
if st.button("Submit"):
    response = get_gemini_response(input_text, image)
    st.subheader("Response is")
    st.write(response)
