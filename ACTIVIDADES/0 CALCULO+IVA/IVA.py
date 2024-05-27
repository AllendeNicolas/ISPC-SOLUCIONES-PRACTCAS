precio_producto = float (input ("cargar precio de producto"))

IVA = 21

total_producto = ((precio_producto * IVA) / 100) + precio_producto

print (total_producto)