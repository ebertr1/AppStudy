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
    
@app.route('/clientlist')
def clientlist():
    return render_template('client-list.html')

@app.route('/clientsearch')
def clientsearch():
    return render_template('client-search.html')

@app.route('/clientupdate')
def clientupdate():
    return render_template('client-update.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/itemlist')
def itemlist():
    return render_template('item-list.html')

@app.route('/itemnew')
def itemnew():
    return render_template('item-new.html')

@app.route('/itemsearch')
def itemsearch():
    return render_template('item-search.html')

@app.route('/itemupdate')
def itemupdate():
    return render_template('item-update.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/reservationlist')
def reservat():
    return render_template('reservation-list.html')

@app.route('/reservationnew')
def reservationnew():
    return render_template('reservation-new.html')

@app.route('/reservationpending')
def reservationpending():
    return render_template('reservation-pending.html')

@app.route('/reservationsearch')
def reservationsearch():
    return render_template('reservation-search.html')

@app.route('/reservationupdate')
def reservationupdate():
    return render_template('reservation-update.html')

@app.route('/userlist')
def userlist():
    return render_template('user-list.html')

@app.route('/usernew')
def usernew():
    return render_template('user-new.html')

@app.route('/usersearch')
def usersearch():
    return render_template('user-search.html')

@app.route('/userupdate')
def userupdate():
    return render_template('user-update.html')



# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
