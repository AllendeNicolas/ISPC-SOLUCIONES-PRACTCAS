Algoritmo CalcularCostoPintura
    Definir alto_pared, ancho_pared, mano_obra_m2, superficie_total_pared, costo_total_pintor Como Real
	
    Escribir "Ingresar altura de la estructura: "
    Leer alto_pared
	
    Escribir "Ingresar ancho de la estructura: "
    Leer ancho_pared
	
    Escribir "Ingrese costo de Mano de obra: "
    Leer mano_obra_m2
	
    superficie_total_pared <- alto_pared * ancho_pared
    Escribir "SUPERFICIE TOTAL: ", superficie_total_pared
	
    costo_total_pintor <- superficie_total_pared * mano_obra_m2
    Escribir "EL COSTO TOTAL DE MANO DE OBRA DEL PINTOR ES: $", costo_total_pintor
	
FinAlgoritmo
