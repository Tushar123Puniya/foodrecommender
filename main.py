import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title('NutriAi Planner')

text = """NutriAi Planner creates personalized meal plans and schedules to match your food
preferences, helping you meet your nutritional goals efficiently. Utilize our Al-driven calorie
calculator to streamline your diet planning process."""
st.write(text)

st.header('Experience personalized meal planning today')

if st.button('Register'):
    switch_page('signup_page')

if st.button('Already a member. Sign In'):
    switch_page('login_page')

