import streamlit as st

# Specify the link you want to redirect to
redirect_link = "http://localhost:8501/"

# Automatically redirect to the specified link using JavaScript
redirect_script = f'''
    <script>
        window.location.href = "{redirect_link}";
    </script>
'''

# Display the redirect script
st.markdown(redirect_script, unsafe_allow_html=True)
