import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd

# Cargar credenciales desde los secretos
google_credentials = st.secrets["google_credentials"]
credentials = Credentials.from_service_account_info(google_credentials)

# Autorizar con gspread
client = gspread.authorize(credentials)

st.title("Formulario para bebé Angie")

# Inputs del formulario
nombre = st.text_input("Ingresa tu nombre")
apellido = st.text_input("Ingresa tu apellido")
fecha_nacimiento = st.date_input("Ingresa tu fecha de nacimiento", min_value=pd.to_datetime("1900-01-01"))
genero = st.radio("Selecciona tu género", ["Masculino", "Femenino"])
profesion = st.selectbox("Selecciona tu profesión", ["Ingeniero", "Psicóloga", "Arquitecto", "Diseñadora"])
notificar = st.checkbox("¿Deseas ser notificado?")


