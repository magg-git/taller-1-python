num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#if num1 > num2:
    #num1, num2 = num2, num1 (extensión para que num1 siempre sea mayor que num2)

for i in range (num1, num2 + 1):
    if i % 2 == 0:
        print(i, "es un par.")
    else:
        print(i, "es un impar.")
