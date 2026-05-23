# Importamos el módulo que contiene el algoritmo matemático para generar
# números aleatoriamente y la libreria NumPy
import random
import Numpy as np   
       
# Imprimimos un aviso de lo que el algoritmo hará
print("\nHola! Calcularemos el determinante de una matríz NxN"
      " tu me dirás el número (N) que prefieras")

# Ciclo infinito que se romperá hasta que el usuario ingrese un dato válido
while True:
    try:
        numero = int(input(
            "Ingresa la cantidad positiva de elementos que desees: ")
                          )
        if numero > 0:
            print("----------¡Número válido!----------\n")
            break
        else:
            print("¡El número debe ser positivo!\n")  
    except ValueError:
        print("¡Ese no es un número!")
        print("Ingresa solamente dígitos\n")

# Creamos el método para llenar la matríz
def fill_matrix(numero):
    matriz = []

# Ciclo para crear las filas
    for _ in range(numero):  
        fila = []
        
# Ciclo para crear las columnas
        for _ in range(numero):
            numeros_aleatorios = random.randint(1, 20) 
            fila.append(numeros_aleatorios)
        matriz.append(fila)
    return matriz

matriz_terminada = fill_matrix(numero)
for fila in matriz_terminada:
    print(fila)
    
matriz_numpy = np.array(matriz_terminada)

determinante = np.linalg.det(matriz_numpy)
print("\nEl determinante de la matriz es: ", round(determinante, 2)) 
    
