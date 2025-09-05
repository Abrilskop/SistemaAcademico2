from flask import Flask
from controladores.escuela_controller import escuela_bp  # Importa el Blueprint de Escuela
from controladores.estudiante_controller import estudiante_bp  # Importa el Blueprint de Estudiante
from controladores.curso_controller import curso_bp  # Importa el Blueprint de Curso
from controladores.matricula_controller import matricula_bp  # Importa el Blueprint de Estudiante

app = Flask(__name__)

# Registra el Blueprint de Escuela
app.register_blueprint(escuela_bp)

# Registra el Blueprint de Estudiante
app.register_blueprint(estudiante_bp)

# Registra el Blueprint de Curso
app.register_blueprint(curso_bp)

# Registra el Blueprint de Matricula
app.register_blueprint(matricula_bp)

if __name__ == '__main__':
    app.run(debug=True)
