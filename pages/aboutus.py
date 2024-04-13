import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Welcome to Our Recommender")

tabs = ["About Us","Nutrition Calculator","Meal recommendation"]
selected_tab = st.sidebar.radio("Navigation", tabs)
if selected_tab == "Nutrition Calculator":
    switch_page('home')
elif selected_tab=="Meal recommendation":
    switch_page('food recommendation')

st.write('Hello we are team of excited individuals who wants to serve you with best food options.')