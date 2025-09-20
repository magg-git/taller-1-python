num = int(input("Ingrese un número entero: "))
contador = 0
n = abs(num) #¿qué es abs? Va a darnos un resultado positivo siempre

if n == 0:
    contador = 1
else:
    while n > 0:
        n //= 10 #¿Para qué sirve el //? // es división entera, agarra la parte entera de la división
        contador += 1

print("el número ", num, "tiene ", contador, "digito(s)")

print(18 // 5)


