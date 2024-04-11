import sqlite3
import streamlit as st
from pages.recommendation_model import recommendation
from pages.home import insert

def update():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    delete_query = "DELETE FROM users WHERE email = ?"
    cursor.execute(delete_query, (st.session_state['email'],))
    conn.commit()
    cursor.close()
    conn.close()
    insert()
    
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
    update()
    recommended_dishes = recommendation(features)
    
    st.write("### Recommended Dishes:")
    for dish in recommended_dishes:
        st.write("- " + dish)
        
st.page_link("main.py", label="Home", icon="🏠")   
