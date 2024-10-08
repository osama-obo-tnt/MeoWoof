import streamlit as st
import requests
import markdown 
from datetime import datetime

# API endpoints
CHAT_API_URL = 'https://alrightosama.pythonanywhere.com/chat'
DATE_API_URL = 'https://alrightosama.pythonanywhere.com/date'
NAME_API_URL = 'https://alrightosama.pythonanywhere.com/name'

st.title("Mewoff Pet System")

# Sidebar for navigation
option = st.sidebar.selectbox("Choose an action", ("Chat", "Predict Date", "Suggest Names"))

if option == "Chat":
    st.sidebar.header("Chat with Veterinary AI")
    user_id = st.sidebar.text_input("User ID")
    conv_id = st.sidebar.text_input("Conversation ID")
    query = st.sidebar.text_area("Enter your query")

    if st.sidebar.button("Submit"):
        if user_id and conv_id and query:
            with st.spinner("Processing..."):
                response = requests.post(CHAT_API_URL, json={
                    "user_id": user_id,
                    "conv_id": conv_id,
                    "query": query
                })
            if response.status_code == 200:
                html_content = response.text
                st.markdown(markdown.markdown(html_content), unsafe_allow_html=True)
            else:
                st.write("Error:", response.status_code)
        else:
            st.write("Please fill all fields.")

elif option == "Predict Date":
    st.sidebar.header("Predict Delivery Date")
    user_id = st.sidebar.text_input("User ID")
    conv_id = st.sidebar.text_input("Conversation ID")

    # Day picker
    day = st.sidebar.selectbox("Select Day", list(range(1, 32)))

    # Month picker
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month = st.sidebar.selectbox("Select Month", months)

    # Combine day and month into a string
    mating_date = f"{day} {month}"

    animal_type = st.sidebar.selectbox("Select Animal Type", ("Cat", "Dog"))

    if st.sidebar.button("Submit"):
        if user_id and conv_id and mating_date and animal_type:
            with st.spinner("Processing..."):
                response = requests.post(DATE_API_URL, json={
                    "user_id": user_id,
                    "conv_id": conv_id,
                    "query": str(mating_date),
                    "type": animal_type
                })
            if response.status_code == 200:
                html_content = response.text
                st.markdown(markdown.markdown(html_content), unsafe_allow_html=True)  
            else:
                st.write("Error:", response.status_code)
        else:
            st.write("Please fill all fields.")

elif option == "Suggest Names":
    st.sidebar.header("Suggest Names for Your Pet")
    user_id = st.sidebar.text_input("User ID")
    conv_id = st.sidebar.text_input("Conversation ID")
    query = st.sidebar.text_area("Enter description for name suggestions")

    if st.sidebar.button("Submit"):
        if user_id and conv_id and query:
            with st.spinner("Processing..."):
                response = requests.post(NAME_API_URL, json={
                    "user_id": user_id,
                    "conv_id": conv_id,
                    "query": query
                })
            if response.status_code == 200:
                html_content = response.text
                st.markdown(markdown.markdown(html_content), unsafe_allow_html=True)  
            else:
                st.write("Error:", response.status_code)
        else:
            st.write("Please fill all fields.")
