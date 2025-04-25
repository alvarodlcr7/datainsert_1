import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
import datetime

# Título de la app
st.title("Formulario para bebé Angie")

# Inputs del formulario
nombre = st.text_input("Ingresa tu nombre")
apellido = st.text_input("Ingresa tu apellido")
fecha_nacimiento = st.date_input("Ingresa tu fecha de nacimiento", min_value=datetime.date(1900, 1, 1))
genero = st.radio("Selecciona tu género", ["Masculino", "Femenino"])
profesion = st.selectbox("Selecciona tu profesión", ["Ingeniero", "Psicóloga", "Arquitecto", "Diseñadora"])
notificar = st.checkbox("¿Desea ser notificado?")

# Cargar credenciales desde los secretos
google_credentials = st.secrets["google_credentials"]
credentials = Credentials.from_service_account_info(google_credentials)

# Autenticación y conexión con Google Sheets
client = gspread.authorize(credentials)
sheet = client.open_by_key("14xnYln4DPcPcjzCBpgK2zVi-y2z5ilT6kdVPFxQEU5o").sheet1

# Acción al hacer clic en "Registrar"
if st.button("Registrar"):
    nuevo_registro = [
        nombre,
        apellido,
        str(fecha_nacimiento),
        genero,
        profesion,
        str(notificar)
    ]
    
    sheet.append_row(nuevo_registro)
    st.success("✅ Registro guardado con éxito en Google Sheets!")

    # Mensaje personalizado
    st.text(f"""Hola {nombre} {apellido}, tu fecha de nacimiento es {fecha_nacimiento}, tu género es {genero}, tu profesión es {profesion}.
    ¡Te adoro mucho!""")
