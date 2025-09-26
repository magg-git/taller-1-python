saldo = 1000
opcion = 0

while opcion != 4:
    
    print("Bienvenido(a) a TuBanco")

    print("--MENÚ--")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Consignar dinero")
    print("4. Salir")

    opcion = int(input("Elija una opción: ")) #sin esto, el bucle se haría infinito, pero igual tenemos que declarar que la variable tiene un valor para poder iniciar el bucle
                
    match opcion:
        case 1:
            print("Su saldo actual es: ", saldo)
        case 2:
            retiro = float(input("Indique la cantidad que desee retirar: ")) #pasa lo mismo del ejercicio 1 aquí 
            if retiro > saldo:
                print("Fondos insuficientes.")
            elif retiro <= 0:
                print("El retiro debe ser mayor a 0.")
            else:
                saldo -= retiro
                print("Retiro exitoso. Su nuevo saldo es: ", saldo)
        case 3: 
            consig = float(input("Indique la cantidad que desee consignar: "))
            saldo += consig
            print("Consignación exitosa. Su nuevo saldo es: ", saldo )
        case 4:
            print("Gracias por usar TuBanco, ¡hasta pronto!")
        case _:
            print("Opción inválida. Por favor intente de nuevo.")





