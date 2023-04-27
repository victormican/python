from modelo2 import Modelo
from vista import Vista

class Salon:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.reservas = []

    def reservar(self, fecha, hora_inicio, hora_fin):
        reserva = {"fecha": fecha, "hora_inicio": hora_inicio, "hora_fin": hora_fin}
        self.reservas.append(reserva)

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista()

    def iniciar_aplicacion(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()
            if opcion == "1":
                datos_salon = self.vista.pedir_datos_salon()
                salon = Salon(*datos_salon)
                self.modelo.agregar_salon(salon)
            elif opcion == "2":
                salones = self.modelo.obtener_salones()
                self.vista.mostrar_salones(salones)
            elif opcion == "3":
                datos_reserva = self.vista.pedir_datos_reserva()
                try:
                    self.modelo.reservar_salon(*datos_reserva)
                    self.vista.mostrar_confirmacion()
                except Exception as e:
                    self.vista.mostrar_error(str(e))
            elif opcion == "4":
                break
            else:
                print("Opción inválida")

controlador = Controlador()
controlador.iniciar_aplicacion()
