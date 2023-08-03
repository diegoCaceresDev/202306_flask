from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html", y = 8, x = 8)

@app.route("/<rows>/<col>/<color1>/<color2>/")

def ajedrez(rows, col, color1, color2):
    return render_template("base.html", y = int(rows), x = int(col), color1 = color1, color2 = color2)


if __name__=="__main__":   
    app.run(debug=True) 