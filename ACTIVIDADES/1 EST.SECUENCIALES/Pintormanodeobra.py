"""En este algoritmo, incluiremos las siguientes variables de entrada. En primer lugar (alto_pared), para conocer la altura de la pared del Galpón. En segundo lugar otra variable con el nombre (ancho_pared), para conocer el ancho de la pared del Galpon. por otra parte, generamos un variable que contenga el costo de la mano de obra de dicho pintor, por metro cuadrado (mano_obra_m2). Luego creamos una variable (superficie_total_pared), con el fin de conocer, cual es la superficie total de la pared, donde multiplicaremos al ancho por el alto de dicha estructura. Y en ultima instancia, para conocer el costo total de la mano de obra del pintor (costo_total_pintor), multiplicaremos, el costo de la mano de obra por, la superficie total de la pared del galpón. """

alto_pared = float (input ("Ingresar altura de la estructura: "))
ancho_pared = float (input ("Ingresar ancho de la estructura: "))

mano_obra_m2 = float (input ("Ingrese costo de Mano de obra: "))

superficie_total_pared = alto_pared * ancho_pared

print ("SUPERFICIE TOTAL:" , superficie_total_pared)

costo_total_pintor = superficie_total_pared * mano_obra_m2

print ("EL COSTO TOTAL DE MANO DE OBRA DEL PINTOR ES: $"  , costo_total_pintor)