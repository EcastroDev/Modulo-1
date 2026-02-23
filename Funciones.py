import streamlit as st

def evaluar_presupuesto(presupuesto, gasto):
    """
    Evalúa si un gasto se encuentra dentro del presupuesto.

    Parámetros:
    - presupuesto: monto disponible
    - gasto: monto utilizado

    Retorna:
    - True o False según el cumplimiento
    - Diferencia entre presupuesto y gasto
    """
    diferencia = presupuesto - gasto
    if gasto <= presupuesto:
        return True, diferencia
    else:
        return False, diferencia

def crear_actividad(nombre, tipo, presupuesto, gasto_real):
    """
    Crea una actividad financiera como diccionario e indica
    si cumple o no el presupuesto.
    """
    if gasto_real <= presupuesto:
        estado = "Dentro del presupuesto"
    else:
        estado = "Excede el presupuesto"

    return {"Nombre": nombre,"Tipo": tipo,"Presupuesto": presupuesto,"Gasto Real": gasto_real,"Estado": estado}

def calcular_retorno(actividad, tasa, meses):
    """
    Calcula el retorno esperado de una actividad.

    Fórmula:
    retorno = presupuesto * tasa * meses
    """
    retorno = actividad["Presupuesto"] * tasa * meses
    return retorno

class Actividad:
    """
    Clase que representa una actividad financiera.
    """

    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        """
        Constructor de la clase Actividad.
        """
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    def esta_en_presupuesto(self):
        """
        Verifica si la actividad cumple con el presupuesto.
        """
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self):
        """
        Retorna la información de la actividad en forma de diccionario.
        """
        return {
            "Nombre": self.nombre,
            "Tipo": self.tipo,
            "Presupuesto": self.presupuesto,
            "Gasto Real": self.gasto_real
        }