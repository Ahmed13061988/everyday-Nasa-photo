import streamlit as st
import requests

api_key = "3AuQ5ZIS3nUbXB2qYXKEB6vkNCw1SD8l88c3tEgq"

url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}&count=10"

response = requests.get(url)

content = response.json()


col1, col2, col3 = st.columns((20, 1, 1))

with col1:
    st.title(content[0]["title"])
    st.image(content[0]["hdurl"])
    st.write(content[0]["explanation"])
