import sqlite3
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.recommendation_model import recommendation
from pages.home import about_us

def insert():
    print(st.session_state['email'])
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

def update():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    delete_query = "DELETE FROM users WHERE email = ?"
    cursor.execute(delete_query, (st.session_state['email'],))
    conn.commit()
    cursor.close()
    conn.close()
    insert()

# Add CSS for positioning the logout button
import streamlit as st

tabs = ["Meal recommendation","Nutrition Calculator"]
selected_tab = st.sidebar.radio("Navigation", tabs)
if selected_tab == "Nutrition Calculator":
    switch_page('home') 
    
st.subheader("Tell us something more") 
taste_preference_type = ['Not Selected','sweet','sour','salty','bitter','savory']
id = taste_preference_type.index(st.session_state['taste_preference'])
taste_preference = st.selectbox('What taste best suits you?:', taste_preference_type,index=id)
st.session_state['taste_preference'] = taste_preference

user_ethenicity_type = ['Not Selected','Chinese','Malays','Malayapura','Arab','Bumiputera','Malay','Negrito','Bhumi malayu','Batak','Iban','Indian','Indonesian','Tamils','Bugis','Javanese','Kedahan malays','Thai']
id = user_ethenicity_type.index(st.session_state['ethnicity'])
ethenicity = st.selectbox('Please select your ethenicity?:', user_ethenicity_type,index= id)
st.session_state['ethnicity'] = ethenicity

user_location_type = ['Not Selected','Johor','Kedah','Kelantan','Malacca','Negeri Sembilan','Pahang','Penang','Perak','Perlis','Sabah','Sarawak','Selangor','Terengganu']
id = user_location_type.index(st.session_state['location'])
location = st.selectbox('Please select your region?:', user_location_type, index=id)
st.session_state['location'] = location

disease_type = ['No Disease','Diabetes','High Blood Pressure','Low Blood Pressure','Hyper Tension']
id = disease_type.index(st.session_state['disease'])
disease = st.selectbox('Please select any kind of disease you have?:', disease_type,index=id)
st.session_state['disease'] = disease

items_mapping={
    'one to three':3,
    'four to six': 6,
    'seven to ten': 10,
    'ten +': 12,
}

number_of_items_type = ['one to three','four to six','seven to ten','ten +']
number_of_items = st.selectbox('How many meal options would you like to see?',number_of_items_type)
st.session_state['number_of_items']=items_mapping[number_of_items]

features = st.session_state['features']

features['ethenicity']=ethenicity
features['taste preference']=taste_preference
features['disease']=disease
features['location']=location

submit_button = st.button('Submit')

if submit_button:
    st.success("Thank you for your preferences! Here are some recommended dishes for you:")

    # Generate recommended food items based on user preferences
    if not st.session_state['new user']:
        update()
    else:
        insert()
        
    recommended_dishes = recommendation(features)
    
    st.write("### Recommended Dishes:")
    for dish in recommended_dishes:
        st.write("- " + dish)

st.page_link("main.py", label="Logout")   