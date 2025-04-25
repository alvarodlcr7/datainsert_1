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
credentials = Credentials.from_service_account_info(google_credentials)

# Autorizar con gspread
client = gspread.authorize(credentials)

# Abrir la hoja de cálculo
sheet = client.open("Formulario para bebé Angie").sheet1

# Al hacer clic en el botón
if st.button("Registrar"):
    # Agregar los datos como una nueva fila
    sheet.append_row([
        nombre,
        apellido,
        str(fecha_nacimiento),
        genero,
        profesion,
        "Sí" if notificar else "No"
    ])

    st.success("✅ Registro guardado con éxito en Google Sheets!")

    st.text(f"""Hola {nombre} {apellido}, tu fecha de nacimiento es {fecha_nacimiento}, tu género es {genero}, tu profesión es {profesion}.
¡Te adoro mucho! 💖""")

# Mostrar todos los registros actuales de la hoja
valores = sheet.get_all_values()
st.subheader("📋 Registros actuales")
st.write(pd.DataFrame(valores[1:], columns=valores[0]))


