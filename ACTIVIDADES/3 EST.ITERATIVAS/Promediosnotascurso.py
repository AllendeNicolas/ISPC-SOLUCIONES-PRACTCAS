#Se solicita realizar un programa que calcule el promedio de notas del curso Y evalue rendimiento del curso en general.

"""EPS: ENTRADA: cant_estudiantes, notas_suma.
      SALIDA: 1) suma de notas y promedio del curso.
           2) evaluación del rendimiento general.
PROCESO: cant_estudiantes guarda la cantidad de estudiantes.
=> Mediante un bucle for se solicitan las notas de cada estudiante y se acumulan en la suma de las notas en notas_suma.
=> Calculamos el promedio dividiendo la suma de las notas entre la cantidad de estudiantes.
Luego, evaluamos el rendimiento según los criterios establecidos."""

cant_estudiantes = int(input("Ingrese la cantidad de estudiantes que han rendido el examen: "))

notas_suma = 0

# Notas de estudiante

for x in range(cant_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {x + 1} (0-10): "))
    notas_suma += nota

promedio = notas_suma / cant_estudiantes

# Evaluación del rendimiento

if promedio > 8:
    print(f"El rendimiento es Elevado. Promedio: {promedio:.2f}")
elif 6 <= promedio <= 8:
    print(f"El rendimiento es Aceptable. Promedio: {promedio:.2f}")
else:
    print(f"El rendimiento es Bajo. Promedio: {promedio:.2f}")