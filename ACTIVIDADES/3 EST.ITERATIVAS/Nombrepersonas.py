"""EPS: Se solicita al usuario que ingrese nombres uno tras otro. Si el usuario escribe “fin”, el bucle se detiene y muestra todos los nombres ingresados
ENTRADA: nombres = [], nombre = input, 
SALIDA: Mostrar lista con Nombres ingresados
PROCESO"""

# Lista vacía para almacenar los nombres
nombres = []

nombre = input("INGRESA LOS NOMBRES QUE DESEES: (Escribe 'fin' para terminar): ")

# Seguimos pidiendo nombres, hasta que se ingrese FIN.
while nombre.lower() != "fin":
    nombres.append(nombre)  # Agrega el nombre a la lista
    nombre = input("Ingresa otro nombre (o escribe 'fin' para terminar): ")

# Lista con nombres ingresados.
print("Los nombres ingresados son:")
for n in nombres:
    print(n)