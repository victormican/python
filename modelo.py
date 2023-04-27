import datetime


# Definir una lista de salones comunales
salones_comunales = ["Salón Comunal 1", "Salón Comunal 2", "Salón Comunal 3"]

# Definir una lista de reservaciones
reservaciones = []


# Función para mostrar los salones comunales disponibles para una fecha específica
def mostrar_salones_disponibles(fecha_seleccion):
    print("Salones comunales disponibles:")
    for i, salon_comunal in enumerate(salones_comunales):
        if salon_comunal not in [r["salon_comunal"] for r in reservaciones if r["fecha_seleccion"] == fecha_seleccion]:
            print(str(i + 1) + ". " + salon_comunal)


# Ciclo principal del programa
while True:
    # Pedir al usuario que ingrese la fecha de selección
    fecha_seleccion = input("Ingrese la fecha de selección (formato dd/mm/yyyy), o escriba 'fin' para salir: ")
    if fecha_seleccion == "fin":
        break
    fecha_seleccion = datetime.datetime.strptime(fecha_seleccion, "%d/%m/%Y")

    # Mostrar los salones comunales disponibles para la fecha de selección actual
    mostrar_salones_disponibles(fecha_seleccion)

    # Pedir al usuario que seleccione un salón comunal
    while True:
        seleccion = input("Seleccione un salón comunal (1-" + str(
            len(salones_comunales)) + "), o escriba 'cambiar' para cambiar la fecha: ")
        if seleccion == "cambiar":
            break
        indice_salon = int(seleccion) - 1

        # Verificar que el índice sea válido
        if indice_salon < 0 or indice_salon >= len(salones_comunales):
            print("Selección inválida.")
        elif salones_comunales[indice_salon] in [r["salon_comunal"] for r in reservaciones if
                                                 r["fecha_seleccion"] == fecha_seleccion]:
            print("El salón comunal ya está reservado para esa fecha.")
        else:
            # Pedir al usuario que ingrese su nombre
            nombre = input("Ingrese su nombre: ")
            cedula = input("Ingrese su cedula: ")
            # Guardar la reservación
            reservaciones.append({
                "fecha_seleccion": fecha_seleccion,
                "salon_comunal": salones_comunales[indice_salon],
                "nombre": nombre,
                "cedula": cedula,

            })

            # Mostrar la información de la reservación
            print("Salón comunal apartado:")
            print("Nombre: " + nombre)
            print("Nombre: " + cedula)
            print("Salón comunal: " + salones_comunales[indice_salon])
            print("Fecha de selección: " + fecha_seleccion.strftime("%d/%m/%Y"))
            break

    # Si el usuario decidió cambiar la fecha de selección, pedirle que ingrese la nueva fecha
    if seleccion == "cambiar":
        fecha_seleccion = input("Ingrese la nueva fecha de selección (formato dd/mm/yyyy): ")
        fecha_seleccion = datetime.datetime.strptime(fecha_seleccion, "%d/%m/%Y")
        mostrar_salones_disponibles(fecha_seleccion)
