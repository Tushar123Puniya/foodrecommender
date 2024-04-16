from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import sqlite3
from streamlit_extras.switch_page_button import switch_page
import webbrowser

def open_url(url):
    webbrowser.open_new_tab(url)
    
def authenticate_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve the password for the given email
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()  # Fetch the first row

    # Check if the email exists in the database
    
    if result is not None:
        # Extract the password from the result
        stored_password = result[0]

        # Compare the stored password with the provided password
        if stored_password == password:
            cursor.execute("SELECT email FROM users WHERE username = ?", (username,))
            var = cursor.fetchone()
            st.success("Login successful!")
            st.session_state['username'] = username
            st.session_state['email'] = var[0]
            st.session_state['password'] = password
            st.session_state['new user'] = False
            st.session_state['given name'] = True
            switch_page('home')
        else:
            st.error("Incorrect password. Authentication failed.")
    else:
        st.error("Username not registered.")

    # Close the cursor and connection
    cursor.close()
    conn.close()
     
def login():
    st.title('Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        authenticate_user(username,password)
        
    st.page_link("main.py", label="Home", icon="🏠")   
     
def main():
    st.session_state['features']={}
    login()

if __name__ == '__main__':
    # Set page config to wide layout
    st.set_page_config(layout="wide")
    main()
