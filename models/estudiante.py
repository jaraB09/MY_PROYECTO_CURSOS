#app/models/estudiantes.py

from app.mysqlconnection import connnectToMySQL
from flask import flask 
import re #Para la validacion de email

#Nombre de tu base de datos 
DB_NAME = 'esquema_estudiantes_cursos'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.curso_id = data['curso_id']
        self.created_at = data['created_at']
        self.update_at =data['update_at']


     @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, email, curso_id) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(curso_id)s);"
        result = connectToMySQL(DB_NAME).query_db(query, data)
        return result
    
    @classmethod 
    def get_one(cls, estudiante_id):
        query = "SELECT * FROM estudiantes WHERE id = %(id)s;"
        data = {'id': estudiante_id}
        result = connectToMySQL(DB_NAME).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def update (cls, data):
        query = "UPDATE estudiantes SET nombre = %(nombre)s, apellido =%(apellido)s, email =%(email)s, curso_id = %(curso_id)s, update_at = NOW() WHERE id=%(id)s;"

    @classmethod
    def delete(cls, estudiantes):
        query = "DELETE FROM estudiantes WHERE id=%(id)s"
        data = {'id': estudiante_id}
        return connnectToMySQL(DB_NAME).query_db(query, data)
    
    @staticmethod
    def validate_estudiante(estudiante):
        is_valid = True
        if len(estudiante['nomnbre'])< 2:
            flash("El nombre del estudiante debe tener al menos 2 caracteres.", "estudiante_error")
            is_valid = True
        if len (estudiante['apellido'])<2:
            flash("El apellido del estudiante debe tener al menos 2 caracteres.", "estudiante_error")
            is_valid = False
        if not EMAIL_REGEX-match(estudiante['email']):
            flash("Email inválido.", "estudinte_error")
            is_valid = False
            # Verificar si el email ya existe (opcional, pare bueno practica) 
                query = "SELECT * FROM estudiantes WHERE email = %(email)s;"
                data = {'email': estudiante['email']}
        results = connectToMySQL(DB_NAME).query_db(query, data)
        if result and result[0] ['id'] != int (estudiante['id']):
            flash("el email ya esta registrado.","estudiante_error")
            is_valid = False
        if not estudiante['curso_id']:
            flash("Debe seleccionar un curso para el estudiante", "estudiante_error")
            is_valid = False
        return is_valid