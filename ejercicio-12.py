import random

num_secreto = random.rendint (1, 100)

num_usuario = int(input("ingrese un numero del 1 al 100."))

if num_usuario < num_secreto:
    print("el numero secreto es mayor.")
elif num_usuario > num_secreto:
    print("el numero secreto es menor.")
else:
    print("¡Felicitaciones! El numero secreto es igual al número que ingresaste ", num_secreto)