import requests

def enviar_datos(horas, asistencia, participacion):
    data = {
        "horas_estudio": horas,
        "asistencia": asistencia,
        "participacion": participacion
    }
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    return response.json()

print("=== PREDICCIÓN DEL RENDIMIENTO ACADÉMICO ===")
print("1️⃣ Ingresar datos manualmente")
print("2️⃣ Probar varios ejemplos automáticos")
opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    horas = float(input("Horas de estudio: "))
    asistencia = float(input("Porcentaje de asistencia: "))
    participacion = float(input("Nivel de participación (1-10): "))
    resultado = enviar_datos(horas, asistencia, participacion)
    print("📊 Resultado del modelo:", resultado)

elif opcion == "2":
    ejemplos = [
        {"horas_estudio": 5, "asistencia": 70, "participacion": 4},
        {"horas_estudio": 10, "asistencia": 90, "participacion": 8},
        {"horas_estudio": 2, "asistencia": 60, "participacion": 3},
        {"horas_estudio": 15, "asistencia": 95, "participacion": 9}
    ]
    for i, ej in enumerate(ejemplos, start=1):
        print(f"\nEjemplo {i}: {ej}")
        resultado = enviar_datos(ej["horas_estudio"], ej["asistencia"], ej["participacion"])
        print("📊 Resultado del modelo:", resultado)
else:
    print("❌ Opción no válida")
