
import streamlit as st
import Funciones as fun
import pandas as pd
import numpy as np



st.sidebar.image("python-logo.png", width=200)
st.sidebar.title("Menu") #Panel lateral

pagina = st.sidebar.selectbox( "Selecciona una página: ",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]) #Texto en el panel lateral

if pagina == "Home":
    st.title ("Bienvenido a la aplicación de ejercicios en Streamlit") #Subtitulo de la aplicacion
    st.write(
        "**Título del proyecto:** Aplicaciones en Streamlit - Fundamentos de Programación\n\n"
        "**Nombre y Apellidos :** Erick Jonathan Castro Cherres\n\n"
        "**Módulo             :** Python Fundamentals\n\n"
        "**Fecha              :** 22 de febrerodel 2026\n\n"
        "**Descripcion        :** En esta aplicación se presentan diferentes ejercicios utilizando Streamlit, una biblioteca de Python que permite crear aplicaciones web interactivas de manera sencilla. La aplicación incluye un menú lateral con opciones para navegar entre diferentes ejercicios, un slider para ingresar la cantidad de elementos y mostrar un arreglo, y una sección para calcular el interés simple utilizando una función definida en el archivo Funciones.py. Además, se muestra una lista de números enteros basada en la entrada del usuario.\n\n"
        "**Tecnologías utilizadas:** Python, Streamlit, NumPy, Pandas"
    )
elif pagina == "Ejercicio 1":

    st.title("Ejercicio 1: Variables y Condicionales")

    presupuesto = st.number_input("Ingrese el presupuesto en soles (S/)", min_value=0.0,step=0.01)

    gasto = st.number_input("Ingrese el gasto en soles (S/)", min_value=0.0, step=0.01)

    if st.button("Evaluar condición"):
        resultado, diferencia = fun.evaluar_presupuesto(presupuesto, gasto)

        if resultado:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El gasto excede el presupuesto.")

        st.write(f"Diferencia entre presupuesto y gasto: S/ {diferencia:.2f}") 
        
elif pagina == "Ejercicio 2":

    st.title("Ejercicio 2: Listas y Diccionarios")

    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Personal", "Estudios","Trabajo", "Otro"])
    presupuesto = st.number_input("Presupuesto asignado (S/)", min_value=0.0, step=0.01)
    gasto_real = st.number_input("Gasto real (S/)", min_value=0.0, step=0.01)

    if st.button("Agregar actividad"):
        actividad = fun.crear_actividad(nombre, tipo, presupuesto, gasto_real)
        st.session_state.actividades.append(actividad)
        st.success("Actividad registrada correctamente")

    if st.session_state.actividades:
        st.subheader("Listado de actividades")
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df)

elif pagina == "Ejercicio 3":

    st.title("Ejercicio 3: Funciones y Programación Funcional")
    st.subheader("Cálculo de Retorno Esperado")

    tasa = st.slider("Tasa de retorno",min_value=0.0,max_value=1.0,value=0.10,step=0.01)

    meses = st.number_input("Número de meses",min_value=1,step=1)
    
    if st.button("Calcular retorno esperado"):

        if "actividades" in st.session_state and st.session_state.actividades:

            retornos = list(map(lambda act: fun.calcular_retorno(act, tasa, meses),
                    st.session_state.actividades))

            st.subheader("Retorno esperado por actividad")

            for act, ret in zip(st.session_state.actividades, retornos):
                st.write(f"**{act['Nombre']}** → Retorno esperado: S/ {ret:,.2f}")

        else:
            st.warning("No hay actividades registradas para calcular retornos.")

elif pagina == "Ejercicio 4":

    st.title("Ejercicio 4: Programación Orientada a Objetos")

    if "actividades" in st.session_state and st.session_state.actividades:

        st.subheader("Actividades como objetos")

        for act in st.session_state.actividades:
            actividad_obj = fun.Actividad(act["Nombre"],act["Tipo"],act["Presupuesto"],act["Gasto Real"])

            info = actividad_obj.mostrar_info()
            st.write(f"**Nombre:** {info['Nombre']}")
            st.write(f"**Tipo:** {info['Tipo']}")
            st.write(f"**Presupuesto:** S/ {info['Presupuesto']}")
            st.write(f"**Gasto Real:** S/ {info['Gasto Real']}")

            if actividad_obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("Excede el presupuesto")

    else:
        st.warning("No hay actividades registradas.")