


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

    archivo_excel = "datos.xlsx"

    # Verificamos si el archivo ya existe
    if os.path.exists(archivo_excel):
        # Leer el archivo existente y agregar el nuevo registro
        df_existente = pd.read_excel(archivo_excel)
        df_actualizado = pd.concat([df_existente, pd.DataFrame([nuevo_registro])], ignore_index=True)
    else:
        # Si no existe, creamos uno nuevo
        df_actualizado = pd.DataFrame([nuevo_registro])

    # Guardar en Excel
    df_actualizado.to_excel(archivo_excel, index=False, engine="openpyxl")

    st.success("✅ Registro guardado con éxito")

    st.text(f"""Hola {nombre}{apellido}, tu fecha de nacimiento es {fecha_nacimiento},tu genero es {genero}, tu profesion es {profesion} te adoro" y solo quiero que sepas que te adoro mucho""")
            