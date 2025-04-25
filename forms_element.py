import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd

st.title("Formulario para bebé Angie")

# Inputs del formulario
nombre = st.text_input("Ingresa tu nombre")
apellido = st.text_input("Ingresa tu apellido")
fecha_nacimiento = st.date_input("Ingresa tu fecha de nacimiento", min_value=pd.to_datetime("1900-01-01"))
genero = st.radio("Selecciona tu género", ["Masculino", "Femenino"])
profesion = st.selectbox("Selecciona tu profesión", ["Ingeniero", "Psicóloga", "Arquitecto", "Diseñadora"])
notificar = st.checkbox("¿Deseas ser notificado?")

# Cargar credenciales desde los secretos de Streamlit
google_credentials = st.secrets["google_credentials"]
credentials

