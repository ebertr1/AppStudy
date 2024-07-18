from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
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
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/client-list')
def client_list():
    return render_template('client-list.html')

@app.route('/client-new')
def client_new():
    return render_template('client-new.html')


@app.route('/client-search')
def client_search():
    return render_template('client-search.html')

@app.route('/client-update')
def client_update():
    return render_template('client-update.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/item-new')
def item_new():
    return render_template('item-new.html')

@app.route('/item-list')
def item_list():
    return render_template('item-list.html')

@app.route('/item-search')
def item_search():
    return render_template('item-search.html')

@app.route('/item-update')
def item_update():
    return render_template('item-update.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/reservation-new')
def reservation_new():
    return render_template('reservation-new.html')

@app.route('/reservation-list')
def reservation_list():
    return render_template('reservation-list.html')

@app.route('/reservation-search')
def reservation_search():
    return render_template('reservation-search.html')

@app.route('/reservation-pending')
def reservation_pending():
    return render_template('reservation-pending.html')

@app.route('/reservation-update')
def reservation_update():
    return render_template('reservation-update.html')

@app.route('/user-new')
def user_new():
    return render_template('user-new.html')

@app.route('/user-list')
def user_list():
    return render_template('user-list.html')

@app.route('/user-search')
def user_search():
    return render_template('user-search.html')

@app.route('/user-update')
def user_update():
    return render_template('user-update.html')



@app.route('/datos-excel')
def datos_excel():
    return render_template('datos-excel.html')

@app.route('/inde', methods=['GET', 'POST'])
def inde():
    if request.method == 'POST':
        # Verificar si se ha enviado un archivo
        if 'excel_file' not in request.files:
            return render_template('inde.html', error='No se ha seleccionado ningún archivo.')

        file = request.files['excel_file']

        # Verificar si se ha enviado un archivo vacío
        if file.filename == '':
            return render_template('inde.html', error='No se ha seleccionado ningún archivo.')

        # Verificar si el archivo es Excel
        if not file.filename.endswith(('.xls', '.xlsx')):
            return render_template('inde.html', error='El archivo seleccionado no es un archivo Excel válido.')

        try:
            # Leer el archivo Excel en un DataFrame
            df = pd.read_excel(file, sheet_name=None)
            
            # Renderizar la plantilla HTML con los datos del DataFrame
            return render_template('datos-excel.html', excel_data=df)

        except Exception as e:
            return render_template('inde.html', error=f'Error al procesar el archivo Excel: {str(e)}')

    return render_template('inde.html')

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
