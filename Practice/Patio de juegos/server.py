from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def iniciar():
    return "Agrega /play al HTML para iniciar el juego"

@app.route('/play/<times>')
def play(times):
    
    return render_template('main.html', times= int(times))

if __name__ == "__main__":
    app.run(debug=True)
