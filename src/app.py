from flask import Flask, render_template, request, redirect, url_for
from config import config

# Crear la aplicación Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Configurar la aplicación desde el objeto de configuración
app.config.from_object(config['development'])

# Definir las rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
        return render_template('login.html')
    else:
        return render_template('login.html')

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
