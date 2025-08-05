from app.mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "matiasponetelaspilas"

# Importa y registra tus objectos tus blueprint (controllers)
from app.controllers import cursos_controller
from app.contorllers import estudiantes_controller

#Registra los blueprint
app.register_blueprint(cursos_controller.cursos.bp)
app.register_blueprint(estudiantes_controller.estudiantes.bp)
