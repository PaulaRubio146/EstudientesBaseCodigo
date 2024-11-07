from db_connection import MySQLConnectionSingleton
from estudiante_dto import EstudianteDTO

class EstudianteDAO:
    def __init__(self):
        self.connection = MySQLConnectionSingleton.get_instance()
        self.cursor = self.connection.cursor()

    def insertar_estudiante(self, estudiante: EstudianteDTO):
        self.cursor.callproc("InsertarEstudiante", (
            estudiante.cedulas,
            estudiante.nombres,
            estudiante.apellidos,
            estudiante.direccion_residencia,
            estudiante.coordenadas_residencia[0],  # latitud
            estudiante.coordenadas_residencia[1],  # longitud
            estudiante.direccion_trabajo,
            estudiante.coordenadas_trabajo[0],    # latitud
            estudiante.coordenadas_trabajo[1]     # longitud
        ))
        self.connection.commit()
        print(f"Estudiante {estudiante.nombres} {estudiante.apellidos} insertado correctamente.")

    def obtener_estudiantes_con_distancia(self):
        # Llamar al procedimiento almacenado
        self.cursor.callproc("ObtenerEstudiantesConDistancia")

        estudiantes = []
        for result in self.cursor.stored_results():
            for row in result.fetchall():
                # Extraer los datos de la fila y agregar a la lista
                cedula, nombres, apellidos, direccion_residencia, direccion_trabajo, distance = row
                estudiante = {
                    "cedula": cedula,
                    "nombres": nombres,
                    "apellidos": apellidos,
                    "direccion_residencia": direccion_residencia,
                    "direccion_trabajo": direccion_trabajo,
                    "distance": distance
                }
                estudiantes.append(estudiante)

        return estudiantes
    
