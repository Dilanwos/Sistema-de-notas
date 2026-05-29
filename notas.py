# =====notas.py====


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas (list): Lista de notas numéricas.

    Returns:
        float: Promedio de las notas.
    """
    if not notas:
        return 0

    return sum(notas) / len(notas)


def clasificar_nota(nota):
    """
    Clasifica una nota según su rendimiento académico.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        str: Clasificación de la nota.
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
    Verifica si una nota cumple con la mínima aprobación.

    Args:
        nota (float): Nota del estudiante.
        minima_aprobacion (float): Nota mínima para aprobar.

    Returns:
        bool: True si aprueba, False si reprueba.
    """
    return nota >= minima_aprobacion
