"""SOLUCION UTILIZANDO BUCLE WHILE"""

def tabla_multiplicar_while(numero):
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        print(f"{numero}x{contador}={resultado}")
        contador += 1

# Solicitamos al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número entero entre 1 y 10: "))
tabla_multiplicar_while(numero_ingresado)


#SOLUCION USANDO BUCLE FOR


def tabla_multiplicar_for(numero):
    for contador in range(1, 11):
        resultado = numero * contador
        print(f"{numero}x{contador}={resultado}")

# Solicitamos al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número entero entre 1 y 10: "))
tabla_multiplicar_for(numero_ingresado)