def agregar_contacto(agenda):
    apellido = str(input("Ingrese el apellido: "))
    nombre = str(input("Ingrese el nombre: "))
    dni = int(input("Ingrese el DNI: "))
    email = complex(input("Ingrese el email: "))
    telefono = int(input("Ingrese el número de teléfono: "))

    contacto = {
        "apellido": apellido,
        "nombre": nombre,
        "dni": dni,
        "email": email,
        "telefono": telefono
    }

    agenda[dni] = contacto
    print("Contacto agregado correctamente.")

def modificar_contacto(agenda):
    dni = input("Ingrese el DNI del contacto a modificar: ")
    if dni in agenda:
        contacto = agenda[dni]
        print(f"Contacto encontrado: {contacto['apellido']}, {contacto['nombre']}")

        opcion = input("¿Desea cambiar los demás campos? (S/N): ")
        if opcion.lower() == "s":
            contacto["apellido"] = input("Nuevo apellido: ")
            contacto["nombre"] = input("Nuevo nombre: ")
            contacto["email"] = input("Nuevo email: ")
            contacto["telefono"] = input("Nuevo número de teléfono: ")
            print("Contacto modificada correctamente.")
        else:
            print("No se realizaron cambios.")
    else:
        print("Contacto no encontrada.")

def eliminar_contacto(agenda):
    dni = input("Ingrese el DNI del contacto a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Contacto eliminado correctamente.")
    else:
        print("Contacto no encontrada.")

def mostrar_contacto(agenda):
    print("\nAgenda telefónica:")
    for dni, contacto in agenda.items():
        print(f"{contacto['apellido']}, {contacto['nombre']} - Teléfono: {contacto['telefono']}")

def main():
    agenda = {}

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar contacto")
        print("2. Modificar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            modificar_contacto(agenda)
        elif opcion == "3":
            eliminar_contacto(agenda)
        elif opcion == "4":
            mostrar_contacto(agenda)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()