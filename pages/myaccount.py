import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sqlite3
from pages.signup_page import insert

# Validation function
def validate_inputs(name, email, existing_username, existing_mail, password, old_password, new_password, confirm_password):
    errors = []

    # Check if name contains only Latin characters
    if name and not name.isalpha():
        errors.append('Please use only English alphabets in the name')

    # Check if username or email already exists
    if existing_username or existing_mail:
        if existing_mail:
            errors.append('Email already registered')
        if existing_username:
            errors.append('Username already exists')

    # Check if email format is valid
    if email and not email.endswith('.com'):
        errors.append('Enter a valid email')

    # Check if password length is at least 8 characters
    if new_password and len(new_password) < 8:
        errors.append('Password length must be at least 8 characters long')

    # Check if old password matches the stored password
    if old_password != password:
        errors.append('Enter correct password')

    # Check if new password matches confirm password
    if new_password != confirm_password:
        errors.append('Password mismatch between new password and confirm password')

    return errors

# Create tabs for "About Us" and "Meal Recommendation"
tabs = ["My Account","Nutrition Calculator","Meal recommendation","About Us"]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab=="About Us":
    switch_page('aboutus')
elif selected_tab=="Nutrition Calculator":
    switch_page('home')
elif selected_tab=='Meal recommendation':
    if st.session_state['name']!="":
            switch_page('food recommendation')
    else:
        st.error('!Please fill information of home page first',icon="🚨")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

email = st.session_state['email']
username = st.session_state['username']
# Streamlit app layout
st.title("Update your profile information")

# Input fields for user data
name = st.text_input("Name")
newusername = st.text_input("Username")
newemail = st.text_input("Email")

new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")
existing_username=False
existing_mail=False
old_password = st.text_input("Old Password", type="password")
cursor.execute("SELECT password FROM users WHERE email=?", (email,))
var = cursor.fetchone()
password = var[0]

if  email!=newemail and newemail:
    cursor.execute("SELECT * FROM users WHERE email = ?", (newemail,))
    existing_mail = cursor.fetchone()

if username!=newusername and username:
    cursor.execute("SELECT * FROM users WHERE username = ?", (newusername,))
    existing_username = cursor.fetchone()

if st.button("Update"):
    errors = validate_inputs(name, newemail, existing_username, existing_mail, password, old_password, new_password, confirm_password)
    if errors:
        for error in errors:
            st.error(error)
    else:
        # Perform update operation
        if name:
            st.session_state['name']=name
        if newusername:
            st.session_state['username'] = newusername
        if newemail:
            st.session_state['email'] = newemail
        if new_password:
            st.session_state['password'] = new_password
        insert(email)
        
        st.success('Information updated Sucessfully !!!')
                       