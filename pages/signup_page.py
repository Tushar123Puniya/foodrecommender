from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import sqlite3

def insert(mail):
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    if mail:
        cursor.execute("DELETE FROM users WHERE email = ?", (mail,))
        conn.commit()
    conn.commit()
    cursor.close()
    conn.close()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    user_data = {
        'email': st.session_state['email'],
        'username': st.session_state['username'],
        'name': st.session_state['name'],
        'password': st.session_state['password'],
        'age': st.session_state['age'],
        'weight': st.session_state['weight'],
        'height': st.session_state['height'],
        'gender': st.session_state['gender'],
        'activity_type': st.session_state['activity_type'],
        'goal': st.session_state['goal'],
        'ethnicity': st.session_state['ethnicity'],
        'taste_preference': st.session_state['taste_preference'],
        'disease': st.session_state['disease'],  # Assuming user doesn't have any disease
        'location': st.session_state['location']
    }

    # Write SQL INSERT statement
    insert_query = """INSERT INTO users 
                        (email,username, password, name, age, weight, height, gender, activity_type, goal, ethnicity, taste_preference, disease, location) 
                    VALUES 
                        (:email, :username, :password, :name, :age, :weight, :height, :gender, :activity_type, :goal, :ethnicity, :taste_preference, :disease, :location)"""

    cursor.execute(insert_query, user_data)
        
    # Commit the transaction to save the changes
    conn.commit()
    
    cursor.close()
    conn.close()
# Validation function
def validate_inputs(existing_user,existing_mail,email, password, confirm_password):
    errors = []

    if existing_user or existing_mail:
        if existing_mail:
            errors.append('Email already registered')
        else:
            errors.append('Username already exists')
            
    # Check if email format is valid
    if not email.endswith('.com'):
        errors.append('Enter a valid email')

    if password!=confirm_password:
        errors.append('Password mismatch password and confirm password are not same.')

    # Check if password length is at least 8 characters
    if len(password) < 8:
        errors.append('Password length must be at least 8 characters long')

    return errors

def signup_user(username,email, password):
    st.session_state['username'] = username
    st.session_state['email'] = email
    st.session_state['password'] = password
    st.session_state['name'] = ""
    st.session_state['gender'] = 'Female'
    st.session_state['age'] = 15
    st.session_state['weight'] = 45
    st.session_state['height'] = 160
    st.session_state['activity_type'] = 'Lightly active (light exercise/sports 1-3 days a week)'
    st.session_state['goal'] = 'Maintain'
    st.session_state['ethnicity'] = 'Indian'
    st.session_state['location'] = 'Johor'
    st.session_state['taste_preference'] = 'Not Selected'   
    st.session_state['disease']='No Disease'   
    insert(None)
    st.success("Sign up successful!")
    switch_page('home')

 
def main():
    st.title('Sign Up')
    st.session_state['features']={}
    username = st.text_input('Username')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_mail = cursor.fetchone()
          
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    if st.button('Sign Up'):
        errors = validate_inputs(existing_user,existing_mail, email,password,confirm_password)
        if errors:
            for error in errors:
                st.error(error)
        else:
            signup_user(username,email,password)
    
    st.page_link("main.py", label="Home", icon="🏠")   

if __name__ == '__main__':
    # Set page config to wide layout
    st.set_page_config(layout="wide")
    main()
