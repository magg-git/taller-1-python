num = int(input("Ingrese un número entero: "))
n = abs(num) #Va a darnos el valor absoluto, muy útil en caso de que se ingrese un negativo

contador = 0

if n == 0:
    contador = 1
else:
    while n > 0:
        n //= 10 #// es división entera, agarra la parte entera de una división
        contador += 1

print("el número ", num, "tiene ", contador, "digito(s).")




