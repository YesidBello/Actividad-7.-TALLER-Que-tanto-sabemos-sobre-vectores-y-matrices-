
Vendedores = int(input("Ingrese el número de vendedores: "))
Años = int(input("Ingrese el número de años: "))

matriz_ventas = []

print("\n------ Ingreso Datos de Ventas ------")
for i in range(Vendedores):
    ventas_vendedor = []
    print(f"Vendedor {i + 1}:")
    for j in range(Años):
        venta = float(input(f"  Ventas del año {j + 1}: "))
        ventas_vendedor.append(venta)
    matriz_ventas.append(ventas_vendedor)
    
total_por_vendedor = []
total_por_ano = [0] * Años
gran_total = 0

for i in range(Vendedores):
    suma_vendedor = 0
    for j in range(Años):
        valor = matriz_ventas[i][j]
        suma_vendedor += valor         
        total_por_ano[j] += valor      
        gran_total += valor            
    total_por_vendedor.append(suma_vendedor)    
    
print("\n------ RESULTADOS ------")  

for i in range(Vendedores):
    print(f"Total ventas Vendedor {i + 1}: ${total_por_vendedor[i]:.2f}")
print("-" * 30)  

for j in range(Años):
    print(f"Total ventas Año {j + 1}: ${total_por_ano[j]:.2f}")
print("-" * 30)

print(f"Gran total de ventas de la empresa: ${gran_total:.2f}")