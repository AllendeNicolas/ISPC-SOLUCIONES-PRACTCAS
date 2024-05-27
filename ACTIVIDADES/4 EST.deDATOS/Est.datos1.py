nombres = []

# Por favor, ingresa Diéz nombres
for i in range(10):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    # Verificar si el nombre ya está en la lista
    if nombre in nombres:
        print(f"El nombre '{nombre}' ya fue ingresado. Intente con otro.")
    else:
        nombres.append(nombre)

# Muestra lista de nombres
print("\nNombres ingresados:")
for nombre in nombres:
    print(nombre)

    """EL CODIGO CONTINUA, ELIMINANDO LOS NOMBRES QUE SE ENCUENTRAN TERCERO Y ULTIMO EN LA LISTA"""

# Eliminar el tercer y último nombre de la lista
if len(nombres) >= 3:
    del nombres[2]  # Elimina tercer nombre
    del nombres[-1]  # Elimina último nombre

# Ordena la lista
nombres.sort()

# Muestra lista actualizada
print("\nNombres ingresados (sin el tercer y último nombre):")
for nombre in nombres:
    print(nombre)