"""En le siguiente algoritmo, generamos las siguientes variables de Entrada. en primer lugar, la variable de partidos ganados (partidos_ganados), donde se muestran la cantidad de triunfos del equipo. Otra variable, para los partidos perdidos (partidos_perdidos), y por último, una variable más, para los partidos en donde el resultado fue empate (partidos_empate). Luego generar una variable, para conocer la cantidad  de  partidos disputados (suma_catidad_partidos), y por último, una función que me entregue, el resultado de los puntos obtenidos (total_puntos), de acuerdo al resultado obtenido en cada encuentro."""

partidos_ganados = int (input ("INGRESE TRIUNFOS DEL EQUIPO: "))
partidos_perdidos = int (input ("INGRESE DERROTAS DEL EQUIPO: "))
partidos_empate = int (input ("INGRESE EMPATES DEL EQUIPO: "))

suma_cantidad_partidos = partidos_ganados + partidos_perdidos + partidos_empate

print ("LA CANTIDAD DE PARTIDOS DISPUTADOS ES: " , suma_cantidad_partidos , "PARTIDOS")

total_puntos = (partidos_ganados * 3) + (partidos_perdidos * 0) + (partidos_empate * 1)

print ("CANTIDAD DE PUNTOS ACUMULADOS EN EL TORNEO: " , total_puntos , "PUNTOS")
