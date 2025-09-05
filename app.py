from flask import Flask
from controladores.escuela_controller import escuela_bp  # Importa el Blueprint de Escuela
from controladores.estudiante_controller import estudiante_bp  # Importa el Blueprint de Estudiante

app = Flask(__name__)

# Registra el Blueprint de Escuela
app.register_blueprint(escuela_bp)

# Registra el Blueprint de Estudiante
app.register_blueprint(estudiante_bp)

if __name__ == '__main__':
    app.run(debug=True)
