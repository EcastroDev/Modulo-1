# Modulo-1

# Proyecto Módulo 1 – Python Fundamentals

## Descripción

Este proyecto es una aplicación interactiva desarrollada con Streamlit como parte del Módulo 1 del curso Python Fundamentals.

El objetivo del proyecto es aplicar los conceptos básicos de programación aprendidos, tales como variables, condicionales, estructuras de datos, funciones, programación funcional y programación orientada a objetos (POO), mediante una aplicación sencilla y didáctica.

La aplicación cuenta con un menú lateral que permite navegar entre distintos ejercicios.

---

## Funcionalidades de la aplicación

### Home
Muestra la presentación general del proyecto, incluyendo:
- Título del proyecto
- Nombre del estudiante
- Módulo del curso
- Fecha
- Descripción del objetivo
- Tecnologías utilizadas

---

### Ejercicio 1 – Variables y Condicionales
Permite ingresar un presupuesto y un gasto, y evalúa si el gasto se encuentra dentro o fuera del presupuesto. Además, muestra la diferencia entre ambos valores.

Conceptos aplicados:
- Variables
- Condicionales
- Funciones

---

### Ejercicio 2 – Listas y Diccionarios
Permite registrar actividades financieras, almacenándolas como diccionarios dentro de una lista.  
Cada actividad incluye su estado respecto al cumplimiento del presupuesto, el cual queda registrado y visible en una tabla.

Conceptos aplicados:
- Listas
- Diccionarios
- Bucles
- Uso de session_state

---

### Ejercicio 3 – Funciones y Programación Funcional
Calcula el retorno esperado de cada actividad registrada utilizando una función definida por el usuario y aplicando programación funcional mediante map y lambda.

Conceptos aplicados:
- Definición de funciones
- Programación funcional
- Uso de map y lambda

---

### Ejercicio 4 – Programación Orientada a Objetos (POO)
Convierte las actividades registradas en objetos de una clase Actividad, utilizando atributos y métodos propios para evaluar el presupuesto y mostrar la información.

Conceptos aplicados:
- Clases y objetos
- Constructores
- Métodos
- Encapsulamiento

---

## Estructura del proyecto

app.py  
Funciones.py  
requirements.txt  
README.md  

- app.py: archivo principal que contiene la interfaz y navegación en Streamlit.  
- Funciones.py: contiene la lógica del programa, funciones y la clase utilizada en POO.  

---

## Tecnologías utilizadas

- Python  
- Streamlit  
- Pandas  
- NumPy  

---

## Instrucciones de ejecución

1. Instalar las dependencias:
   pip install -r requirements.txt

2. Ejecutar la aplicación:
   streamlit run app.py

---

## Autor

Erick Jonathan Castro Cherres  
Año: 2024
