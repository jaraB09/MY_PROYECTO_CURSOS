#app/controllers/estudiantes_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.estudiante import Estudiante
from app.models.curso import Curso #Necesitamos el modelo Curso para el Dropdown

estudiantes_bp = Blueprint('estudiantes', __name__)

# Ruta para mostrar el formulario de un nuevo estudiante
@estudiantes_bp.route('/estudiantes/new')
def new_estudiante():
    cursos= Curso.get_all()  # Obtenemos todos los cursos para el dropdown
    return render_template('estudiantes/new.html', cursos=cursos)

# Ruta para procesar la creación de un nuevo estudiante
@estudiantes_bp.route('/estudiantes/create', methods=['POST'])
def create_estudiante():
    "El ID del estudiante es 0 para la validacion inicial de email unico"
    form_data = request.form.to_dict()
    form_data['id'] = 0 # Para la validación de email en creación
    
    if not Estudiante.validate_estudiante(form_data):
        cursos = Curso.get_all()#vuelve a cargar los cursos si la validacion falla
        return render_template('nuevo_estudiante.html', cursos=cursos, form_data=form_data)
    
    Estudiante.save(request.form)
    flash('Estudiante creado exitosamente', 'success')
    return redirect(url_for('cursos.index'))#redirige a la pagina de cursos

# Ruta para mostrar el formulario de edición de un estudiante
@estudiantes_bp.route('/estudiantes/<int:id>/edit')
def edit_estudiante(estudiante_id):
    estudiante = Estudiante.get_by_id(estudiante_id)