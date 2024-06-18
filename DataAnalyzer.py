import tempfile
import warnings
from vision import *
import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader


def main():
    st.title("Data Analyzer")

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    # fetch file path
    if uploaded_file is not None:
        # use tempfile as CSVloader only accepts a file_path
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

            # initialize CSV loader
            csv_loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={'delimiter': ','})

            # load data into csv loader
            data = csv_loader.load()

            # Debug statement to check content of data
            print("Data:", data)

            # initialize chat interface
            user_input = st.text_input("Your message")

            if user_input:
                get_model_response(data, user_input)
                response = "response"
                st.write(response)


if __name__ == "__main__":
    main()

