import random

num_secreto = random.randint(1, 100) #el randit nos indica el rango del que queremos que se genere el número aleatorio

num_usuario = 0

while num_usuario != num_secreto:
    num_usuario = int(input("Ingrese un numero del 1 al 100: "))      
    if num_usuario < num_secreto:
        print("Muy bajo.")
    elif num_usuario > num_secreto:
        print("Muy alto.")

print("¡Felicitaciones! El numero secreto es: ", num_secreto)