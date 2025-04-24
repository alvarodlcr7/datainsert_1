


import streamlit as st
import os
import pandas as pd


st.title("Formulario para bebe Angie")
nombre=st.text_input("Ingresa tu nombre")
apellido=st.text_input("Ingresa tu apellido")
fecha_nacimiento=st.date_input("Ingresa tu fecha de nacimiento",min_value="1900-01-01")
genero=st.radio("Selecciona tu genero",["maculino","Femenino"])
profesion=st.selectbox("Selecciona tu profesion",["Ingeniero","Psicologa","Arquitecto","Diseñadora"])
notificar=st.checkbox("¿Desea ser notificado")
estudios=None



    # Acción al hacer clic en Registrar
if st.button("Register"):

    # Crear un nuevo registro
    nuevo_registro = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha de nacimiento": fecha_nacimiento,
        "Género": genero,
        "Profesión": profesion,
        "Desea ser notificado": notificar
    }

   # Definir el alcance para Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Cargar las credenciales de Google desde los secretos de Streamlit
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["google_credentials"], scope)

    # Autorizar las credenciales y conectar con Google Sheets
    client = gspread.authorize(credentials)

    # Abre la hoja de cálculo (asegúrate de que el nombre es correcto)
    spreadsheet = client.open("Formulario para bebé Angie").sheet1

    # Agregar el nuevo registro a Google Sheets
    spreadsheet.append_row([nombre, apellido, str(fecha_nacimiento), genero, profesion, notificar])

    st.success("✅ Registro guardado con éxito en Google Sheets!")

    # Mensaje personalizado para el usuario
    st.text(f"""Hola {nombre} {apellido}, tu fecha de nacimiento es {fecha_nacimiento}, tu género es {genero}, tu profesión es {profesion}.
    ¡Te adoro mucho!""")
