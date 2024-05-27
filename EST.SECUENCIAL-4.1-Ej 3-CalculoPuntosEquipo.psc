Algoritmo CalculoPuntosEquipo
    Definir partidos_ganados, partidos_perdidos, partidos_empate, suma_cantidad_partidos, total_puntos Como Entero
	
    Escribir "INGRESE TRIUNFOS DEL EQUIPO: "
    Leer partidos_ganados
	
    Escribir "INGRESE DERROTAS DEL EQUIPO: "
    Leer partidos_perdidos
	
    Escribir "INGRESE EMPATES DEL EQUIPO: "
    Leer partidos_empate
	
    suma_cantidad_partidos = partidos_ganados + partidos_perdidos + partidos_empate
    Escribir "LA CANTIDAD DE PARTIDOS DISPUTADOS ES: ", suma_cantidad_partidos, " PARTIDOS"
	
    total_puntos = (partidos_ganados * 3) + (partidos_perdidos * 0) + (partidos_empate * 1)
    Escribir "CANTIDAD DE PUNTOS ACUMULADOS EN EL TORNEO: ", total_puntos, " PUNTOS"
	
FinAlgoritmo
