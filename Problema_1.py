# Importamos el módulo que contiene el algoritmo matemático para generar
# números aleatoriamente
import random

# Imprimimos un aviso de lo que el algoritmo hará
print("\nHola! Tu me dirás un número (N) y yo haré una lista de (N) números al"
      " azar para luego ordenarlos de mayor a menor")

# Ciclo infinito que se romperá hasta que el usuario ingrese un dato válido
while True:
    try:
        n_elementos = int(input(
            "Ingresa la cantidad positiva de elementos que desees: ")
                          )
        if n_elementos > 0:
            print("----------¡Número válido!----------\n")
            break
        else:
            print("¡El número debe ser positivo!\n")  
    except ValueError:
        print("¡Ese no es un número!")
        print("Ingresa solamente dígitos\n")
        
# Creamos una lista donde se almacenarán los numeros generados aleatoriamente
lista_numeros = []

# Ciclo que genera los números
for _ in range(n_elementos):

    numeros_generados = random.randint(1, 1000)
    lista_numeros.append(numeros_generados)

print("Lista de números al azar: ", lista_numeros)

# Iniciamos un booleano
hubo_intercambio = True

# Creamos un ciclo que finaliza cuando no se haga un intercambio más
while hubo_intercambio:
    hubo_intercambio = False

    for i in range(n_elementos - 1):

        if lista_numeros[i] < lista_numeros[i + 1]:
            lista_numeros[i], lista_numeros[i + 1] = (
                lista_numeros[i + 1],
                lista_numeros[i],
            )
            hubo_intercambio = True
print("\n-----------------------------------------------------------------\n")


print("Lista de números ordenados de mayor a menor: ", lista_numeros)
print("\n")
