from modelo2 import Reservacion

class Controlador:
    def __init__(self):
        self.reservaciones = []

    def agregar_reservacion(self, fecha, salon_comunal, nombre, cedula):
        reservacion = Reservacion(fecha, salon_comunal, nombre, cedula)
        self.reservaciones.append(reservacion)

    def mostrar_salones_disponibles(self, fecha_seleccion):
        salones_comunales = ["Salón Comunal 1", "Salón Comunal 2", "Salón Comunal 3"]
        reservados = [r.salon_comunal for r in self.reservaciones if r.fecha == fecha_seleccion]
        disponibles = [s for s in salones_comunales if s not in reservados]
        return disponibles
