from flask import Flask, render_template # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/success')
def success():
    return "success"


@app.route('/hola/<name>')          
def hola_nombre(name):
    return f'Hola {name}!'

@app.route('/render')
def render_inicio():
    return render_template("inicial.html")



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
