class Vista:
    def mostrar_menu(self):
        print("1. Agregar salón")
        print("2. Ver salones")
        print("3. Reservar salón")
        print("4. Salir")

    def pedir_opcion(self):
        opcion = input("Ingrese una opción: ")
        return opcion

    def pedir_datos_salon(self):
        nombre = input("Ingrese el nombre del salón: ")
        capacidad = int(input("Ingrese la capacidad del salón: "))
        return (nombre, capacidad)

    def pedir_datos_reserva(self):
        salon = input("Ingrese el nombre del salón: ")
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
        hora_inicio = input("Ingrese la hora de inicio (hh:mm): ")
        hora_fin = input("Ingrese la hora de fin (hh:mm): ")
        return (salon, fecha, hora_inicio, hora_fin)

    def mostrar_salones(self, salones):
        for salon in salones:
            print(f"Nombre: {salon.nombre}, Capacidad: {salon.capacidad}, Reservas: {salon.reservas}")

    def mostrar_confirmacion(self):
        print("La reserva se realizó correctamente")

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
