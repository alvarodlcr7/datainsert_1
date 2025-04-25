import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
from datetime import date

# Título
st.title("Formulario para bebé Angie")

# Entradas de usuario
nombre = st.text_input("Ingresa tu nombre")
apellido = st.text_input("Ingresa tu apellido")
fecha_nacimiento = st.date_input("Ingresa tu fecha de nacimiento", min_value=date(1900, 1, 1))
genero = st.radio("Selecciona tu género", ["Masculino", "Femenino"])
profesion = st.selectbox("Selecciona tu profesión", ["Ingeniero", "Psicóloga", "Arquitecto", "Diseñadora"])
notificar = st.checkbox("¿Deseas ser notificado?")

# Botón de registro
if st.button("Registrar"):

    # Obtener credenciales desde secrets
    google_credentials = st.secrets["google_credentials"]

    # Autenticación con Google
    credentials = Credentials.from_service_account_info(google_credentials)
    client = gspread.authorize(credentials)

    # Abre la hoja usando la KEY (no por nombre)
    spreadsheet = client.open_by_key("14xnYln4DPcPcjzCBpgK2zVi-y2z5ilT6kdVPFxQEU5o")
    sheet = spreadsheet.sheet1

    # Agregar datos
    sheet.append_row([
        nombre,
        apellido,
        str(fecha_nacimiento),
        genero,
        profesion,
        "Sí" if notificar else "No"
    ])

    st.success("✅ Registro guardado exitosamente")

    st.text(f"""
    Hola {nombre} {apellido}, tu fecha de nacimiento es {fecha_nacimiento}, tu género es {genero}, y tu profesión es {profesion}.
    ¡Gracias por registrarte!
    """)

