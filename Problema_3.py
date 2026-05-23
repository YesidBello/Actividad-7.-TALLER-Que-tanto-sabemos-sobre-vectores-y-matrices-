import random

respuestas_correctas = [random.randint(1, 5) for _ in range(60)]
respuestas_mate_correctas = respuestas_correctas[:30]
respuestas_verbal_correctas = respuestas_correctas[30:]

cantidad_estudiantes = int(input("Ingresa la cantidad de estudiantes: "))

estudiantes = []

total_puntaje_mate = 0
total_puntaje_verbal = 0
total_puntaje_global = 0

for estudiante in range(cantidad_estudiantes):
    
    registro_estudiantes = {
        "Credencial": estudiante + 1,
        "Matematicas": [random.randint(1, 5) for _ in range(30)],
        "Verbal": [random.randint(1, 5) for _ in range(30)]
        }
    estudiantes.append(registro_estudiantes)
