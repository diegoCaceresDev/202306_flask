from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say(name):
    if isinstance(name, str):
        return f'Hola {name}'


@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    if isinstance(int(number), int) and isinstance(word, str):
        return f'|{word}| '*int(number)

if __name__=="__main__":   
    app.run(debug=True)   

