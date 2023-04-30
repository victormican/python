import datetime

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_salones_disponibles(self, fecha_seleccion):
        salones_disponibles = self.controlador.mostrar_salones_disponibles(fecha_seleccion)
        print("Salones comunales disponibles:")
        for i, salon in enumerate(salones_disponibles):
            print(str(i+1) + ". " + salon)

    def agregar_reservacion(self):
        fecha = input("Ingrese la fecha de selección (formato dd/mm/yyyy): ")
        fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
        self.mostrar_salones_disponibles(fecha)
        seleccion = input("Seleccione un salón comunal (1-3): ")
        indice_salon = int(seleccion) - 1
        nombre = input("Ingrese su nombre: ")
        cedula = input("Ingrese su cedula: ")
        salon_comunal = self.controlador.mostrar_salones_disponibles(fecha)[indice_salon]
        self.controlador.agregar_reservacion(fecha, salon_comunal, nombre, cedula)
        print("Reservación realizada con éxito.")

    def menu_principal(self):
        while True:
            print("Bienvenido a su gestor de Salones Comunales")
            print("Seleccione su opcion :")
            print("1. Reservar salón comunal")
            print("2. Salir")
            seleccion = input("Seleccione una opción: ")
            if seleccion == "1":
                self.agregar_reservacion()
            elif seleccion == "2":
                break
            else:
                print("Selección inválida.")
