from flask import Flask, render_template, redirect, session, request
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = "secreto"

@app.route('/')
def oro_ninja():
    return render_template("base.html")


@app.route("/process_money/", methods=["POST"])
def process_money():
    
    current_datetime = datetime.now()
    session["building"] = request.form["building"]
    
    if "money" not in session:
        session["money"] = 0
        session["activity"] = []
        
    if (session["building"] == "farm"):
        random_money = random.randrange(10, 20)
        session["money"] += random_money
        session["activity"] += [f"Earned {random_money} golds from the {session['building']}! ({current_datetime.strftime('%d/%m/%Y')}, {current_datetime.strftime('%H:%M:%S %p')})."]
        
    if (session["building"] == "cave"):
        random_money = random.randrange(5, 10)
        session["money"] += random_money
        session["activity"] += [f"Earned {random_money} golds from the {session['building']}! ({current_datetime.strftime('%d/%m/%Y')}, {current_datetime.strftime('%H:%M:%S %p')})."]

        
    if (session["building"] == "house"):
        random_money = random.randrange(2, 5)
        session["money"] += random_money
        session["activity"] += [f"Earned {random_money} golds from the {session['building']}! ({current_datetime.strftime('%d/%m/%Y')}, {current_datetime.strftime('%H:%M:%S %p')})."]

        
    if (session["building"] == "casino"):
        change = random.randrange(1, 3)
        random_money = random.randrange(0, 50)
        
        if (change == 1):
            session["money"] += random_money
            session["activity"] += [f"Earned {random_money} golds from the {session['building']}! ({current_datetime.strftime('%d/%m/%Y')}, {current_datetime.strftime('%H:%M:%S %p')})."]

            
        elif (change == 2):
            session["money"] -= random_money
            session["activity"] += [f"Earned {random_money} golds from the {session['building']}! ({current_datetime.strftime('%d/%m/%Y')}, {current_datetime.strftime('%H:%M:%S %p')})."]
    
    print(session["money"])

    return redirect ("/")


@app.route('/reiniciar/')
def reiniciar():
    session.clear()
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)