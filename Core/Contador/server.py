from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'   

@app.route('/')
def contador():
    session['visitas'] = session.get('visitas', 0) + 1
    return render_template("base.html")

@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True) 