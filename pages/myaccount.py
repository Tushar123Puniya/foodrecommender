import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("My Account")

# Create tabs for "About Us" and "Meal Recommendation"
tabs = ["Nutrition Calculator","Meal recommendation","About Us","My Account"]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab=="About Us":
    switch_page('aboutus')
elif selected_tab=="My Account":
    switch_page('myaccount')
elif selected_tab=='Meal recommendation':
    if st.session_state['given name']:
            switch_page('food recommendation')
    else:
        st.error('!Please fill information of home page first',icon="🚨")
else:
    home()

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

username = st.session_state['username']
cursor.execute("SELECT name FROM users WHERE email=?", (email,))
var = cursor.fetchone()
st.session_state['name'] = var[0]

name = st.text_input("Enter Your Name:", st.session_state['name'])
st.session_state['name'] = name