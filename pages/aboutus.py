import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Welcome to NutiAI Planner")

# Create tabs for "About Us" and "Meal Recommendation"
tabs = ["About Us","Nutrition Calculator","Meal recommendation","My Account"]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab=="Nutrition Calculator":
    switch_page('home')
elif selected_tab=="My Account":
    switch_page('myaccount')
elif selected_tab=='Meal recommendation':
    if st.session_state['given name']:
        switch_page('food recommendation')
    else:
        st.error('!Please fill information of nutri calculator page first',icon="🚨")

st.write(
        """
        ## About Us
        A pioneering meal planning platform dedicated to transforming how individuals approach nutrition and wellness. Our mission is to empower our users to make informed dietary choices that align with their health goals and preferences.

        At NutriAI Planner, we leverage the latest advancements in artificial intelligence to deliver personalized meal recommendations based on user-specific data like height, weight, dietary objectives, taste preferences, and dietary restrictions or allergies. This meticulous approach ensures that every meal recommendation is not only nutritionally balanced but also perfectly suited to individual needs and tastes.

        We prioritize user satisfaction and strive for excellence in delivering a seamless experience. Whether you're looking to achieve weight loss, muscle gain, or simply maintain a healthy diet, NutriAI Planner is your trusted partner in achieving your nutritional aspirations.

        Embark on this journey to a healthier and happier lifestyle with NutriAI Planner.
        """
    )
