import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from google.oauth2 import service_account
import random

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # If not initialized, initialize the app
    cred = credentials.Certificate("sprictinkvisualizer-7ca7b98a9bf9.json")
    firebase_admin.initialize_app(cred)
else:
    # If already initialized, get the default app
    default_app = firebase_admin.get_app()


# Now you can continue using the Firebase app
def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp


def send_email(email):
    otp = generate_otp()
    # Load credentials from JSON file
    credentials_file = 'sprictinkvisualizer-7ca7b98a9bf9.json'
    credentials = service_account.Credentials.from_service_account_file(credentials_file)

    # Create SMTP client with SSL
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    try:
        smtp_server.login('scriptinkvisualizer@gmail.com',
                          'kogc mcfm jxfu pyvk')
        message = EmailMessage()
        message['Subject'] = 'OTP for ScriptInkVisualizer Sign-in: ' + otp
        message['From'] = 'scriptinkvisualizer@gmail.com'
        message['To'] = email
        message.set_content("Congratulations on taking the first step towards unleashing your creativity with "
                            "ScriptInkVisualizer! 🚀 \nWe've just sent an OTP to ensure your security.\nYour creative "
                            "journey is about to begin, and we're thrilled to have you onboard.\nYour OTP is:" + otp)

        smtp_server.send_message(message)
        print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        smtp_server.quit()
        return otp


def login(email):  # Define login function to accept email argument
    try:
        auth.get_user_by_email(email)
        st.subheader("Logging in...")
        # Execute the command in the terminal
        command = "streamlit run main.py"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Display the output and error in Streamlit
        st.text("Output:")
        st.text(output.decode())

        st.text("Error:")
        st.text(error.decode())
    except:
        st.warning("Login Failed")


def app():
    st.title("Welcome to ScriptInkVisualizer")
    choice = st.selectbox('Login/Signup', ['Login', 'Signup'])
    sent_otp = ""
    received_otp = ""
    if choice == 'Login':
        email = st.text_input('Email Address')
        if st.button('Send Otp', key="Otp_button"):
            sent_otp = send_email(email)
            print(sent_otp)
            received_otp = st.text_input('OTP', type="password", key='otp_input')
            if st.button('Login', key="Login_button"):
                print("1")
            if sent_otp == received_otp:
                st.success("Login Successful")
                login(email)
                return
            else:
                st.error("Login Unsuccessful. Enter correct OTP.")

    else:
        email1 = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')

        if st.button('Create my account', key='create_account_button'):
            # Perform signup actions here
            send_email(email1)
            # validation(received_otp)
            st.info('Creating account...')

            st.success('Account Created Successfully! Please login using your email and password.')
            st.balloons()


app()
