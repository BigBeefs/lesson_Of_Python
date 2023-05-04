import streamlit as st
from dotenv import load_dotenv
import os
import requests

def main():
    # st.markdown(f'''<style>.stApp {{background-image:url("API/WeatherLogo.png");background-size: cover;}}</style>''',unsafe_allow_html=True)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.dribbble.com/users/1077537/screenshots/5048550/logo.png");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Meteo della Tua Città")
    load_dotenv('API/.env')
    api_key : str = os.getenv('API_KEY')
    
    city = st.text_input('Inserisci il nome della tua Città')
    if city != '':  
        url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        result = requests.get(url.format(city,api_key))
        json = result.json()
        temp = json['main']['temp'] - 273
        temp = round(temp)
            
        st.metric('',temp,'°C')
    
    
if __name__ == "__main__":
    main()