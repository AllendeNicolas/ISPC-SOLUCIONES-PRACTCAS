"""EPS: Desemos saber cual es la temperatura exacta que debe hacer a fuera, para decidir si nos ponemos o no la campera. Si la temperatura es menor o igual a 15 grados centígrados, necesitamos salir abrigados con la campera inflable.
ENTRADA: temperatura <= 15
SALIDA: Usar campera inflable, sino No necesitamos campera inflable.
PROCESO:"""

temperaturA = float(input("Ingresa la temperatura en grados CENTÍGRADOS: "))

if temperaturA <= 15:
    print("¡URGENTE, ESTÁ FRÍO, USA TU CAMPERA!")
else:
    print("No necesitas usar tu campera inflable.")