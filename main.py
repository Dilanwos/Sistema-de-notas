from notas import reporte

numero1 = input("Ingrese la primera nota: ")
numero2 = input("Ingrese la segunda nota: ")
numero3 = input("Ingrese la tercera nota: ")

try:
    notas_estudiante = [float(numero1), float(numero2), float(numero3)]

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
    exit()

# Generar reporte
resultado = reporte(notas_estudiante)

# Mostrar resultados
print("\n=== REPORTE DEL ESTUDIANTE ===")
print(f"Aplicación: {resultado['app']}")
print(f"Versión: {resultado['version']}")
print(f"Promedio: {resultado['promedio']}")
print(f"Clasificación: {resultado['clasificacion']}")
print(f"¿Aprobó?: {resultado['aprobado']}")
