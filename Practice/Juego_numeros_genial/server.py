from flask import Flask, render_template, request, session, redirect, flash
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

def crear_numero_random():
    return random.randint(1, 100)


@app.route("/")
def great_number():
    if "random" not in session:
        session["random"] = crear_numero_random()
    print(session["random"])
    return render_template("great_number.html")


@app.route("/great_quiz/", methods=["POST"])
def great_quiz():
    print(request.form)
    session["number"] = int(request.form["number"])

    if session["number"] > session["random"]:
        flash("Too High")
    elif session["number"] < session["random"]:
        flash("Too Low")
    else:
        flash(f"{session['number']} was the number!")
        session.pop("random")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)