#Autores: Programa realizado por el Equipo2_CodePain
#Version 1.2
#Este programa lee una velocidad y determina si es mayor a 100, imprime "muy rapido" y si es cero, 
# imprime "detenido"

#Entrada
vel = 0 #Variable que almacena la velocidad
vel = float(input()) 

while (vel < 0 or (vel>0 and vel<=100)): #Condicion para velocidades positivas
    print("Error, ingrese otro numero")
    vel = float(input())


#Proceso: Checar si la velocidad es mayor a 100 o igual a 0
#Salida: "Muy rapido" o "Detenido" o nada si no es cero o mayor a cien


if (vel > 100):
    print("Muy rápido")
elif (vel == 0):
    print("Detenido")