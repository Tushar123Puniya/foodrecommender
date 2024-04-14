from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from pages.caloriy_calculate import calculate_calories
import sqlite3

def main():

    # Add background image CSS
    st.markdown(
        """
        <style>
        body {
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to NutriAI Planner")
    
    # Create tabs for "About Us" and "Meal Recommendation"
    tabs = ["Nutrition Calculator","Meal recommendation","About Us"]
    selected_tab = st.sidebar.radio("Navigation", tabs)

    if selected_tab=="About Us":
        switch_page('aboutus')
    elif selected_tab=='Meal Plan Generator':
        if st.session_state['given name']:
                switch_page('food recommendation')
        else:
            st.error('!Please fill information of home page first',icon="🚨")
    else:
        home()
        
def about_us():
    st.write(
        """
        ## About Us
        A pioneering meal planning platform dedicated to transforming how individuals approach nutrition and wellness. Our mission is to empower our users to make informed dietary choices that align with their health goals and preferences.

        At NutriAI Planner, we leverage the latest advancements in artificial intelligence to deliver personalized meal recommendations based on user-specific data like height, weight, dietary objectives, taste preferences, and dietary restrictions or allergies. This meticulous approach ensures that every meal recommendation is not only nutritionally balanced but also perfectly suited to individual needs and tastes.

        We prioritize user satisfaction and strive for excellence in delivering a seamless experience. Whether you're looking to achieve weight loss, muscle gain, or simply maintain a healthy diet, NutriAI Planner is your trusted partner in achieving your nutritional aspirations.

        Embark on this journey to a healthier and happier lifestyle with NutriAI Planner.
        """
    )
  
def home():
    st.write(
        """
        Welcome to our restaurant! We offer a wide range of delicious dishes to satisfy your cravings.
        """
    )            
    
    st.subheader('Tell Us About Yourself')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    if not st.session_state['new user']:
        email = st.session_state['email']
        cursor.execute("SELECT name FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['name'] = var[0]
        
    else:
        st.session_state['name'] = ''
        
    name = st.text_input("Enter Your Name:", st.session_state['name'])
    st.session_state['name'] = name
    
    if not st.session_state['new user']:
        email = st.session_state['email']
        cursor.execute("SELECT gender FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['gender'] = var[0]
        cursor.execute("SELECT age FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['age'] = int(var[0])
        cursor.execute("SELECT weight FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['weight'] = int(var[0])
        cursor.execute("SELECT height FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['height'] = int(var[0])
        cursor.execute("SELECT activity_type FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['activity_type'] = var[0]
        cursor.execute("SELECT goal FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['goal'] = var[0]
        cursor.execute("SELECT ethnicity FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['ethnicity'] = var[0]
        cursor.execute("SELECT taste_preference FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['taste_preference'] = var[0]
        cursor.execute("SELECT disease FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['disease'] = var[0]
        cursor.execute("SELECT location FROM users WHERE email=?", (email,))
        var = cursor.fetchone()
        st.session_state['location'] = var[0]
    
    else:
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
    
    cursor.close()
    conn.close()
    
    gender_type = ['Male', 'Female']
    id = gender_type.index(st.session_state['gender'])
    gender = st.selectbox('Please select your gender:', gender_type,index=id )
    st.session_state['Gender'] = gender
    
    goal_type = ['Gain','Lose','Maintain']
    id = goal_type.index(st.session_state['goal'])
    goal = st.selectbox('What type of specific goal you have in mind about gaining, maintaining or losing weight:', goal_type,index=id)
    st.session_state['goal'] = goal
    
    Age = st.slider('Select your age (in years):', min_value=15, max_value=75, value=st.session_state['age'], step=1)
    st.session_state['age'] = Age
    
    Weight = st.slider("Select your Weight (in kg):", min_value=45, max_value=109, value=st.session_state['weight'], step=1)
    st.session_state['weight'] = Weight
    
    Height = st.slider("Select your Height (in cm):", min_value=160, max_value=191, value=st.session_state['height'], step=1)
    st.session_state['height'] = Height

    activity_type = ['Sedentary (little or no exercise)','Lightly active (light exercise/sports 1-3 days a week)','Moderately active (moderate exercise/sports 3-5 days a week)','Very active (hard exercise/sports 6-7 days a week)','Extra active (very hard exercise/sports & physical job or training twice a day']
    id = activity_type.index(st.session_state['activity_type'])
    activity = st.selectbox('What type of activity best alligned with your schedule:', activity_type,index= id)
    st.session_state['activity_type'] = activity
    
    mapping = {
        'Sedentary (little or no exercise)':1,
        'Lightly active (light exercise/sports 1-3 days a week)':2,
        'Moderately active (moderate exercise/sports 3-5 days a week)':3,
        'Very active (hard exercise/sports 6-7 days a week)':4,
        'Extra active (very hard exercise/sports & physical job or training twice a day':5
    }
    activity = mapping[activity]
    
    features ={
                'Age':Age,
                'Weight':Weight,
                'Gender':gender,
                'Height':Height,
                'Activity type':activity,
                'Goal':goal
            }
    
    st.session_state['features']=features
    calcuate_button = st.button('Calculate my calorie need')
    
    if calcuate_button:
        if not name or not Age or not Height or not Weight or not gender:
            st.error('Please fill in all required fields.')
        else:
            caloriy_need = calculate_calories(features)
            st.write(f'Your daily caloriy need per meal is: {caloriy_need :.2f}')
    
    if name:
        st.session_state['given name'] = True
    # recommend_food = st.button('Recommend me food items')
    # if recommend_food:
    #     if not name or not Age or not Height or not Weight or not gender:
    #         st.error('Please fill in all required fields.')
    #     else:
    #         if  st.session_state['new user']:
    #             insert()
    #         switch_page('food recommendation')


if __name__ == "__main__":
    main()
