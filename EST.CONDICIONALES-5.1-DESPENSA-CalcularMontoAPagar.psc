Algoritmo CalcularMontoAPagar
    Definir leche_unidades, es_jubilado, monto_parcial, montoAPagar Como Entero
	
    Escribir "INGRESE UNIDADES DE LECHE POR CLIENTE: "
    Leer leche_unidades
	
    Escribir "INGRESE 0, SI EL CLIENTE NO ES JUBILADO, CUALQUIER OTRO NUMERO SI EL CLIENTE ES JUBILADO: "
    Leer es_jubilado
	
    monto_parcial <- leche_unidades * 1000
	
    Si (leche_unidades <= 12 y no es_jubilado) Entonces
        montoAPagar <- monto_parcial
    Sino Si ((leche_unidades > 12 Y leche_unidades <= 24) Y NO es_jubilado) Entonces
			montoAPagar <- monto_parcial * 0.9
		Sino Si (leche_unidades > 24 Y NO es_jubilado) Entonces
				montoAPagar <- monto_parcial * 0.85
			Sino Si (leche_unidades <= 12 Y es_jubilado) Entonces
					montoAPagar <- monto_parcial * 0.9
				Sino Si ((leche_unidades > 12 Y leche_unidades <= 24) Y es_jubilado) Entonces
						montoAPagar <- monto_parcial * 0.8
					Sino
						montoAPagar <- monto_parcial * 0.75
					Fin Si
					
					Escribir "El monto sin descuento es: ", monto_parcial
					Escribir "El monto total a pagar es: ", montoAPagar
				Fin si
			Fin si
		Fin si
	Fin Si
FinAlgoritmo
