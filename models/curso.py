from app.config.mysqlconnection import connectToMySQL
from flask import Flask

#Nombre de tu base de datos (!asegurate de que coincida con la que creaste!)
DB_NAME = 'esquema_estudiantes_cursos'

class Curso:
    def __init__(self, data):
        self.id = data ['id']
        self.nombre = data ['nombre']
        self.descripcion = data ['descripcion']
        self.created_at =  data ['created_at']
        self.updated_at = data ['update_at']
        self.estudiantes = [] # Para almacenar los estudiantes asociados a este curso.
    
    #forma de obtener todos los cursos creados por el usuario
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursor ORDER BY nombre ASC;"
        results = connectToMySQL(DB_NAME).query_db(query)
        cursor = []
        if results:
            for curso_data in results:
                cursos.append(cls(curso_data))

        return cursos
    
    @classmethod
    def get_one_with_estudiantes(cls, curso_id)
        query = """
            SELECT c.*, e.id AS estudiantes_id, e.nombres AS  estudiantes_nombres, e.apellido AS estudiante_apellido,e.email  AS estudiante_email
        FROM cursos c
        LEFT JOIN  estudiantes e ON c.id = e.curso_id
        WHERE c.id = %(id)s;
        """
        data = {'id :curso_id'}
        results = connectToMySQL(DB_NAME).query_db(query, data)

        if not results:
            return None
        
        #Crear la instancia del curso una sola vez 
        curso= cls(results[0])# Usamos  el primer resultado para los datos del curso 

        #agrega los estudiantes si existen 

        for row in results:
            if row['estudiantes_id']:# Si hay datos de estudiantes creame este diccionario
                estudiante_data = {
                    'id ': row ['estudiantes_id'],
                    'nombre' : row['estudiantes_nombre'],
                    'apellido' : row['estudiantes_apellido'],
                    'email' : row['estudiantes_email'],
                    'curso_id' :row['id'],# El ID del curso al que pertenece
                    'created_at' : row['created_at'],# Estos campo no estan en el Select del estudiante, heredan del curso o se manejaran en el modelo del estudiante
                    'updated_at' :row['updated_at']

                }


    