
print("1. multiplicación")
print("2. división")
print("3. suma")
print("4. resta")
print("5. exponenciación")

op = int(input("seleccione la operación que quiera ejecutar: "))

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

match op:
    case 1:
       mult = num1 * num2
       print("el resultado de la multiplicación es: ", mult)
    case 2: 
        if num2 == 0:
            print("esta operación no se puede realizar")
        else:
            div = num1 / num2
            print("el resultado de la división es: ", div)
    case 3:
        sum = num1 + num2
        print("el resultado de la suma es: ", sum)
    case 4:
        res = num1 - num2
        print("el resultado de la resta es: ", res)
    case 5:
        exp = num1 ** num2 
        print("el resultado de la exponenciación es: ", exp)
    case _:
        print("por favor elija una opción válida")