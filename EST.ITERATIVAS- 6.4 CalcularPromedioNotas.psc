Algoritmo CalcularPromedioNotas
    Definir num_estudiantes, suma_notas, nota, promedio Como Entero
    Definir i Como Entero
	
    Escribir "Ingrese la cantidad de estudiantes que han rendido el examen: "
    Leer num_estudiantes
	
    suma_notas <- 0
	
    Para i <- 1 Hasta num_estudiantes Con Paso 1 Hacer
        Escribir "Ingrese la nota del estudiante ", i, " (0-10): "
        Leer nota
        suma_notas <- suma_notas + nota
    Fin Para
	
    promedio <- suma_notas / num_estudiantes
	
    Si promedio > 8 Entonces
        Escribir "El rendimiento ha sido elevado. Promedio: ", promedio
	Sino Si promedio >= 6 Y promedio <= 8 Entonces
			Escribir "El rendimiento es aceptable. Promedio: ", promedio
	Sino
		Escribir "El rendimiento es bajo. Promedio: ", promedio
		
	Fin si
	Fin si
	
FinAlgoritmo
