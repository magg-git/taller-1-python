positivos = 0
negativos = 0
ceros = 0

num = int(input("Indique la cantidad de números que desee ingresar: "))

for i in range (1, num + 1):
    numeros = int(input("Ingrese número: ",))
    if numeros > 0:
        positivos += 1
    elif numeros < 0:
        negativos += 1
    elif numeros == 0:
        ceros += 1

print("Total de positivos: ", positivos)
print("Total de negativos: ", negativos)
print("Total de ceros: ", ceros)
