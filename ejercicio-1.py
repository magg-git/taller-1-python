
print("--CALCULADORA--")
print("1. multiplicación")
print("2. división")
print("3. suma")
print("4. resta")
print("5. potenciación")

opcion = int(input("Seleccione la operación que quiera ejecutar: "))

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
#los floats provocan que los resultados salgan con un .0 adiccional, esto no influye en el resultado, pero igual hay que chequearlo

match opcion:
    case 1:
       mult = num1 * num2
       print("El resultado de la multiplicación es: ", mult)
    case 2: 
        if num2 == 0:
            print("Esta operación no se puede realizar.")
        else:
            div = num1 / num2
            print("El resultado de la división es: ", div)
    case 3:
        sum = num1 + num2
        print("El resultado de la suma es: ", sum)
    case 4:
        res = num1 - num2
        print("El resultado de la resta es: ", res)
    case 5:
        exp = num1 ** num2 
        print("El resultado de la potenciación es: ", exp)
    case _:
        print("Por favor elija una opción válida.")