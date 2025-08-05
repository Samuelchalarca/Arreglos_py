print ("hola mundo")
#en python no se nesesita declarar el tipo de dato
#Reales: float - doble
#Float 32 bits, significa de 32 bits almacena en 32 bits "Reserva de memoria"
#Double 64 bits,
#Entero: int 
#Boleanos: bool
#String: str

#Tipos de condicionales
#if
#elif
#Else

#cosas -> match apartir de la version 3.10, se debe tener cuidado con las vercione ya que algunas no son compatibles con versiones diferentes

"""
Ciclos -> ciclos de repeticion
 for=para (Solo con numeros) (de menor a mayor)(Evalua la condicional inicio)
 while mientras (con todo tipo de dato)(Puede sumular un ciclo para)(Evalua la condicional inicio)
 break= romper palabra reservada para python
 continue = continuar palabra reservada en pythom
 pass = no hacer nada
"""
if True:
    print("Hola mundo true")
    edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#condicional compuestos
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Condicional anidados

print("Segun el numero es el rol que debe mostrrar")
opcion = int(input("Ingrese el numero de la opcion:"))
if opcion==1:
    print("Opcion 1 administrador")
    
elif opcion==2:
    print("Opcion 2 usuario") 
elif opcion==3:
    print("Opcion 3 aprendiz")
else:
    print("Opcion no valida")

match opcion:
    case 1:
        print("Es el rol administrador")
    case 2:
        print("Es el rol usuario")
    case 3:
        print("Esl el rol inviado")
    case _:
        print("No es un rol valido")


    
#ciclo or recorrido acendente y desendente 
#acendente
for i in range(1,11):
    print (i)

#decendiente
for i in (10,0-1):
    print(i)

#ejemplo intervalo de 2 en 2
for i in range(1,-11,-2):
    print(i)
    

#Medicion de ejercicio con for
import time
inicio=time.time()
for i in range (5):
    print(i)
fin = time.time()
tiempoFinal = fin-inicio
print("Tiempo de ejecucion", tiempoFinal) 

#Medicion de tiempo Ciclo while
inicio = time.time()
contador = 0
while contador <= 10:
    print (contador)
    contador+=1
fin = time.time()
tiempoFinal = fin - inicio
print("Tiempo de ejecucion:", tiempoFinal)

import sys
import os
time.sleep(5)
if sys.platform == "win32":
    os.system("cls")
else:
    os.system('clear')

#formas de controlar wile 
"""
Por numero reales o enteros
Por boleanos
Por cadenas de texto

No primitivos
listas
tuplos
direccionarios 
sets
rango
Arreglos:Vectores y matrices
"""
#Control letra
palabra=input("Ingrese una palabra:")
while palabra.upper()=="S":
    palabra = input("Ingrese una palabra:")
print("Fin del ciclo while")

#Control por false o True
contador=0
while True:
    if contador == 10:
        break
    else:
        print("El contador no hallegado a 10")
        contador+=1

print("El ciclo while ha terminado Corctamente")