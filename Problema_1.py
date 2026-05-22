import random


while True:
    try:
        n_elementos = int(input(
            "Ingresa la cantidad positiva de elementos que desees: ")
                          )
        if n_elementos > 0:
            print("¡Número válido!")
            break
        else:
            print("¡El número debe ser positivo!")
            
    except ValueError:
        print("¡Ese no es un número!")
        print("Ingresa solamente números")              
                
lista_numeros = []

for _ in range(n_elementos):

    numeros_generados = random.randint(1, 1000)
    lista_numeros.append(numeros_generados)

print("Lista de números al azar: ", lista_numeros)

hubo_intercambio = True

while hubo_intercambio:
    hubo_intercambio = False

    for i in range(n_elementos - 1):

        if lista_numeros[i] < lista_numeros[i + 1]:
            lista_numeros[i], lista_numeros[i + 1] = (
                lista_numeros[i + 1],
                lista_numeros[i],
            )
            hubo_intercambio = True
print("--------------------------------------------------------------------"
      "---------------------------------------------------------------------")
print("--------------------------------------------------------------------"
      "-------------------------------------------------------------------")

print("Lista de números ordenados de mayor a menor: ", lista_numeros)
\

