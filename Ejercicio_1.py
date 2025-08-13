"""
Es una calculadora con las funciones Suma, Resta, Multiplicacion y Division,
con un limpiador de consola que va a hacer un "cls"

Creado por: Ramos Yefry   29/05/2025
"""


import os # proporciona acceso a diversas funciones 
def limpiar_consola(): # es para limpiar la barra
    if os.name == 'nt': # es una variable
        os.system('cls') # "cls" va a hacer la palabra que tenemos que colocar para limpiar la barra


def DATOS(): # los datos que se van a ingresar
    num1 = float(input("ingresar el primer numero:")) # ingresar un numero
    num2 = float(input("ingresar el segundo numero:")) # ingresar el segundo numero 
    return num1, num2 # es para volver a retornar num1 o num2
 

def SUMA(): # La opcion es una suma 
    print("suma") #suma

    num1, num2 = DATOS() #ingresar los numeros
    resultado = num1 + num2 # la operacion es una suma

    print(f"/nRESULTADO: {num1} + {num2} = {resultado}") #muestra la suma de num1 y num2
    input("presione enter para continuar...") #volver al programa de inicio

def RESTA():# la opcion de resta 
    print("resta") #la operacion es una resta

    num1, num2 = DATOS() #los datos que van a ingresar
    resultado = num1 - num2 #la operacion es una resta

    print(f"/nRESULTADO: {num1} - {num2} = {resultado}") # el resultado del num1 y num2
    input("presione enter para continuar...") #volver al programa de inicio

def MULTIPLICACION():#la opcion es una multiplicacion
    print("multiplicacion") #la operacion es una multiplicacion
    num1, num2 = DATOS()#los numeros que van a ingresar 
    resultado = num1 * num2 # la operacion es una multiplicacion

    print(f"/nRESULTADO: {num1} * {num2} = {resultado}") # el resultado de num1 y num2
    input("presione enter para continuar...") #volver al programa de inicio



while True:#estructura
    limpiar_consola() #opcion de limpiar la consola 
    print("Calculadora") #calciuladora
    print(" Bienvenido, Selecionar una opcion:") #despliega el mensaje
    print("1. Suma") #suma
    print("2. Resta") # despliega el mensaje que es una resta
    print("3. Mutiplicacion") # despliega el mensaje que es una multiplicacion
    print("4. Salir")#salir del programa
    opcion = input("ingresar el numero de la opcion deseada:") #ingresar la opcion deseada

    if opcion == '1': #ingresar opcion 1
        SUMA() #suma

    if opcion == '2':# ingresar opcion 2
        RESTA() #resta

    if opcion == '3': #ingresar opcion 3
        MULTIPLICACION()  #multiplicacion  


    elif opcion == '4':#opcion 5
        print("/nSaliendo del sistema... ¡Hasta pronto!")  #despliega un mensaje de salida y despedida 
        break # un bucle "salir"
    else:#estructura
        print("Opcion no validad.") # no deja entrar si no pones una opcion correcta