import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Variables de entorno
APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
MAX_NOTA = float(os.getenv("MAX_NOTA"))
MIN_APROBACION = float(os.getenv("MIN_APROBACION"))


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas (list): Lista de notas numéricas.

    Returns:
        float: Promedio calculado.
    """

    if not notas:
        return 0

    return sum(notas) / len(notas)


def clasificar_nota(nota):
    """
    Clasifica una nota según el rendimiento académico.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        str: Clasificación correspondiente.
    """

    if nota > MAX_NOTA or nota < 0:
        return "Nota inválida"

    if nota >= 4.5:
        return "Excelente"

    elif nota >= 4.0:
        return "Sobresaliente"

    elif nota >= MIN_APROBACION:
        return "Aprobado"

    else:
        return "Reprobado"


def esta_aprobado(nota):
    """
    Verifica si una nota cumple con la mínima aprobación.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        bool: True si aprueba, False si reprueba.
    """

    return nota >= MIN_APROBACION


def reporte(notas):
    """
    Genera un reporte completo del estudiante.

    Args:
        notas (list): Lista de notas.

    Returns:
        dict: Información completa del estudiante.
    """

    promedio = calcular_promedio(notas)

    return {
        "app": APP_NAME,
        "version": VERSION,
        "promedio": round(promedio, 2),
        "clasificacion": clasificar_nota(promedio),
        "aprobado": esta_aprobado(promedio),
    }
