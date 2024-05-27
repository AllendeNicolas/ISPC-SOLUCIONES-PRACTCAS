"""En este ejercicio calcularemos el promedio de materias de un estudiante. El total son 5 materias. Se genera una variable de entrada para cada materia. (nota_materia_1, nota_materia_2, nota_materia_3, nota_materia_4, nota_materia_5, respectivamente). Luego generamos otra variable donde se calcula la suma de todas las Notas (con el nombre: sumatoria_notas_materias), y luego generamos otra variable, donde dividimos el resultado de la varible anterior, por 5,que es la cantidad de materias del estudiante, (denominamos a esta variable: promedio_materias), con el que obtendremos el promedio general de las carrera del alumno. """

nota_materia_1 = float (input("Cargar nota de la materia N° 1: "))
nota_materia_2 = float (input("Cargar nota de la materia N° 2: "))
nota_materia_3 = float (input("Cargar nota de la materia N° 3: "))
nota_materia_4 = float (input("Cargar nota de la materia N° 4: "))
nota_materia_5 = float (input("Cargar nota de la materia N° 5: "))

sumatoria_notas_materias = nota_materia_1 + nota_materia_2 + nota_materia_3 + nota_materia_4 + nota_materia_5

promedio_materias = sumatoria_notas_materias / 5 #cantidad de maerias del alumno#
print ("EL PROMEDIO DE LA CARRERA ES:" , promedio_materias)
