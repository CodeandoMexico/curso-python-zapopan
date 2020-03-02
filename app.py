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
        e1 = int(form.e1.data)
        p1 = float(form.p1.data)
        e2 = int(form.e2.data)
        p2 = float(form.p2.data)
        e3 = int(form.e3.data)
        p3 = float(form.p3.data)
        u = float(form.u.data)

        entradas = [e1, e2, e3]
        pesos = [p1, p2, p3]

        producto_interior = 0
        for i in range(len(entradas)):
            producto_interior = producto_interior + (entradas[i] * pesos[i])

        if producto_interior >= u:
            resultado = True
        else:
            resultado = False

        return render_template("resultado.html", res=resultado)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
