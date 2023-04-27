class Modelo:
    def __init__(self):
        self.salones = []

    def agregar_salon(self, salon):
        self.salones.append(salon)

    def obtener_salones(self):
        return self.salones

    def reservar_salon(self, salon, fecha, hora_inicio, hora_fin):
        for s in self.salones:
            if s.nombre == salon:
                s.reservar(fecha, hora_inicio, hora_fin)
                break
