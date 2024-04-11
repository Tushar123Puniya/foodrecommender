from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import sqlite3
from pages.home import main as home_main

def signup_user(username,email, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        st.error("This username already registered. Please use a different one.")
    else:
        # If email doesn't exist, store the email for storing in future
        # print(st.session_state['email'])
        st.session_state['username'] = username
        st.session_state['email'] = email
        st.session_state['password'] = password
        st.session_state['new user'] = True
        st.success("Sign up successful!")
        switch_page('home')
        
    # Close the cursor and connection
    cursor.close()
    conn.close()
 
 
def main():
    st.title('Sign Up')
    st.session_state['features']={}
    username = st.text_input('Username')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if st.button('Sign Up'):
        if not email.endswith('.com'):
            st.error('Please enter a valid email')
        elif password!=confirm_password:
            st.error('Password mismatch')
        else:
            signup_user(username,email,password)

if __name__ == '__main__':
    # Set page config to wide layout
    st.set_page_config(layout="wide")
    main()