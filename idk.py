class Proyecto:
    def __init__(self, nombre, descripcion, fechalimi):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechalimi = fechalimi
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def consultar_tareas_pendientes(self):
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completada]
        return tareas_pendientes

    def consultar_tareas_completadas(self):
        tareas_completadas = [tarea for tarea in self.tareas if tarea.completada]
        return tareas_completadas

proyecto_actual = Proyecto()
tarea1 = Proyecto("Crear botón", "Agregale uso al botón", "20-04-2024")
tarea2 = Proyecto("Diseña una interfaz", "Realizar una buena interfaz completa", "18-04-2024")
proyecto_actual.agregar_tarea(tarea1)
proyecto_actual.agregar_tarea(tarea2)
tarea1.marcar_completada()