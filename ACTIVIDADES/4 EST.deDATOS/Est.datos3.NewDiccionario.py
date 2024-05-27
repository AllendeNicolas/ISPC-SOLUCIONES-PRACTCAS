Familia_datos = {
   1: {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'dni': '12345678',
    'email': 'juan@gmail.com',
    'fecha_nacimiento': '1970-07-28'
   } ,

    2: {
    'nombre': 'Carlos',
    'apellido': 'Pérez',
    'dni': '1234561233',
    'email': 'charly@gmail.com',
    'fecha_nacimiento': '1985-06-13'
    } ,

    3: {
    'nombre': 'Mariano',
    'apellido': 'Pérez',
    'dni': '12356333678',
    'email': 'mar@hotmail.com',
    'fecha_nacimiento': '1971-11-15'
    },

    4: {
    'nombre': 'Monica',
    'apellido': 'Pérez',
    'dni': '1235555678',
    'email': 'mony@yahoo.com',
    'fecha_nacimiento': '1980-06-20'
    }
}

# Acceder a los datos de un Familiar:

print("Nombre:", Familia_datos[1]['nombre'])
print("Apellido:", Familia_datos[1]['apellido'])
print("DNI:", Familia_datos [1]['dni'])
print("Fecha de nacimiento:", Familia_datos[1]['fecha_nacimiento'])
print("Email:", Familia_datos[1]['email'])
