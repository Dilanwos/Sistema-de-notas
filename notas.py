# =====notas.py====


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    """
    if not notas:
        return 0

    return sum(notas) / len(notas)


def clasificar_nota(nota):
    """
    Clasifica una nota según el rendimiento académico.
    """
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 4.0:
        return "Sobresaliente"
    elif nota >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def esta_aprobado(nota, minima_aprobacion=3.0):
    """
    Verifica si una nota aprueba.
    """
    return nota >= minima_aprobacion


def reporte(notas):
    """
    Genera un reporte completo del estudiante.

    Args:
        notas (list): Lista de notas.

    Returns:
        dict: Información del promedio, clasificación y aprobación.
    """
    promedio = calcular_promedio(notas)

    return {
        "promedio": round(promedio, 2),
        "clasificacion": clasificar_nota(promedio),
        "aprobado": esta_aprobado(promedio),
    }
