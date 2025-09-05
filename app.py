from flask import Flask
from controladores.escuela_controller import escuela_bp

app = Flask(__name__)
app.register_blueprint(escuela_bp)

if __name__ == '__main__':
    app.run(debug=True)