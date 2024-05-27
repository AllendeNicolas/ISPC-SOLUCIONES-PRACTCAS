"""EPS
Entrada: leche_unidades - entero, es_jubilado - Logico
Salida: montoAPagar E Real
Proceso:"""

leche_unidades = int (input ("INGRESE UNIDADES DE LECHE POR CLIENTE: "))
es_jubilado = int (input ("INGRESE 0, SI EL CLIENTE NO ES JUBILADO, CUALQUIER OTRO NUMERO SI EL CLIENTE ES JUBILADO: "))

monto_parcial = leche_unidades * 1000
print (f"leche_unidades {leche_unidades} es_jubilado {es_jubilado}" )

if (leche_unidades <= 12 and not es_jubilado):
    print ("leche_unidades <= 12 and not es_jubilado")
    montoAPagar = monto_parcial
elif ((leche_unidades > 12 and leche_unidades <=24) and not es_jubilado):
    print ("(leche_unidades > 12 and leche_unidades <=24) and not es_jubilado")
    montoAPagar = monto_parcial * 0.9
elif (leche_unidades > 24 and not es_jubilado):
    print ("leche_unidades > 24 and not es_jubilado")
    montoAPagar = monto_parcial * 0.85
elif (leche_unidades <= 12 and es_jubilado):
    print ("leche_unidades <= 12 and es_jubilado")
    montoAPagar = monto_parcial * 0.9
elif ((leche_unidades > 12 and leche_unidades <= 24) and es_jubilado):
    print ("(leche_unidades > 12 and leche_unidades <= 24) and es_jubilado")
    montoAPagar = monto_parcial * 0.8
elif (leche_unidades > 24 and es_jubilado):
    print ("leche_unidades > 24 and es_jubilado")
    montoAPagar = monto_parcial * 0.75

print (f"El monto sin desc. es:{monto_parcial} y el total:{montoAPagar}")