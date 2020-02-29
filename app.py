from flask import Flask
from flask import render_template
from flask import request
from forms import NeuronaForm

app = Flask(__name__)

skills = [
    "Python",
    "Inteligencia Artificial",
    "Datos"
]


@app.route("/")
def url_principal():
    return render_template("intro.html", habilidades=skills)

@app.route("/contacto")
def url_contacto():
    return render_template("base.html")

@app.route("/neurona", methods=['GET', 'POST'])
def neurona():
    form = NeuronaForm(request.form)
    if request.method == 'GET':
        return render_template("neurona.html")
    if request.method == 'POST':
        e1 = form.entrada_1.data
        e2 = form.entrada_2.data

        entradas = [e1, e2]

        return render_template("resultado.html", entradas=entradas)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
