precio_producto = float (input ("cargar precio de producto: "))

IVA = 21

IVA_MAYOR = 10.5

if precio_producto >= 10000:
    print ("Corresponde IVA MAYORISTA") 
else:
    print ("Corresponde IVA MENOR")

total_producto = ((precio_producto * IVA) / 100) + precio_producto

print (total_producto)

total_producto = ((precio_producto * IVA_MAYOR) / 100) + precio_producto

print (total_producto)