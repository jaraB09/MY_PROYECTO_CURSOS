#app/controllers/cursos_controller.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.curso import Curso

cursos_bp = Blueprint('cursos', __name__)

#ruta para mostrar todos los cursos y formularios de la creacion 
@cursos_bp.route('/')
@cursos_bp.route('/cursos')
def index():
    cursos = Curso.get_all()
    return render_template('cursos/index.html', cursos=cursos)

#ruta para procesar la creacion de un nuevo curso
@cursos_bp.route('/cursos/new',methods =['POST'])
def create_curso():
    if not Curso.validate_curso(request.form):
        return redirect(url_for('cursos.index'))

#ruta para mostrar un curso especifico y sus estudiantes
@cursos_bp.route('/cursos/<int:curso_id>')
def show_curso(curso_id):
    curso = Curso.get_one_with_estudiantes(curso_id)
    if not curso:
        flash("Curso no encontrado.","error")
        return redirect(url_for('cursos.index'))
    return render_template('mostrar_curso.html', curso=curso)

#ruta para mostrar el formulario de edicion de un curso
@cursos_bp.route('/cursos/<int:curso_id>/edit')
def edit_curso(curso_id):
    curso = Curso.get_one_whith_estudiantes(curso_id)#usamos el mismo 
    if not curso:
        flash("Curso no encontrado.","error")
        return redirect(url_for('cursos.index'))
    return render_template('cursos/edit.html', curso=curso)

#ruta para procesar la acttualizacion de un curso

@cursos_bp.route('/cursos/<int:curso_id>/update', methods=['POST'])
def update_curso(curso_id):
    if not Curso.validate_curso(request.form):
        return redirect(url_for('cursos.edit_curso', curso_id=curso_id))
    
    data = {
        'id': curso_id,
        'nombre': request.form['nombre'],
        'descripcion': request.form['descripcion']
    }
    Curso.update(data)
    flash("Curso actualizado correctamente.", "success")
    return redirect(url_for('cursos.show_curso', curso_id=curso_id))

#ruta para eliminar un curso
@cursos_bp.route('/cursos/<int:curso_id>/delete', methods=['POST'])
def delete_curso(curso_id):
    if Curso.delete(curso_id):
        flash("Curso eliminado correctamente.", "success")
    else:
        flash("Error al eliminar el curso.", "error")
    return redirect(url_for('cursos.index'))