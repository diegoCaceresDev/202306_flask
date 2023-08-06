from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'clave secreta' 

@app.route("/")
def encuesta():
    return render_template('encuesta.html')


@app.route("/process/", methods=['POST'])
def process():
    print(request.form)
    session["nombre"] = request.form['nombre']
    session["ciudad"] = request.form['ciudad']
    session["lenguaje"] = request.form['lenguaje']
    session["comentarios"] = request.form['comentarios']
    return render_template("datos_encuesta.html")



if (__name__ == "__main__"):
    app.run(debug=True)

