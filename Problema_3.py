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

for estudiante in estudiantes:
    puntaje_mate = 0
    puntaje_verbal = 0
    
    for i in range(30):
        if estudiante["Matematicas"][i] == respuestas_mate_correctas[i]:
            puntaje_mate += 1
    for i in range(30):
        if estudiante["Verbal"][i] == respuestas_verbal_correctas[i]:
            puntaje_verbal += 1
           
    estudiante["Puntaje_Mate"] = puntaje_mate
    estudiante["Puntaje_Verbal"] = puntaje_verbal
    estudiante["Puntaje_Total"] = puntaje_mate + puntaje_verbal
    
    total_puntaje_mate += puntaje_mate
    total_puntaje_verbal += puntaje_verbal
    total_puntaje_global += estudiante["Puntaje_Total"] 

promedio_mate = total_puntaje_mate / cantidad_estudiantes
promedio_verbal = total_puntaje_verbal / cantidad_estudiantes
promedio_total = total_puntaje_global / cantidad_estudiantes

for estudiante in estudiantes:
    if estudiante["Puntaje_Total"] >= promedio_total:
        print(f"Credencial: {estudiante['Credencial']} | Puntaje Total: {estudiante['Puntaje_Total']}")
        
estudiante_top = max(estudiantes, key=lambda x: x["Puntaje_Total"])
print(f"\n🏆 El MAYOR puntaje fue de {estudiante_top['Puntaje_Total']}, obtenido por la Credencial {estudiante_top['Credencial']}")
 