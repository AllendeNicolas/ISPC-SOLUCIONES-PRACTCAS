"""Este código solicita al usuario un número y luego muestra todos los números desde 0 hasta el número ingresado.
EPS: 
ENTRADA: numero = y contador=
SALIDA:muestra los numeros hasta el solicitado por el usuario.
PROCESO:"""

# Solicitar al usuario un número
numero = int(input("INGRESE EL NÚMERO DESEADO: "))

# CONTADOR

contador = 0

# CONTADOR MENOR O IGUAL, AL NUMERO INGRESADO:

while contador <= numero:
    print(contador)
    contador += 1
