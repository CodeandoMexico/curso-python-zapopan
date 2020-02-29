from wtforms import Form
from wtforms import TextField

class NeuronaForm(Form):
    entrada_1 = TextField('entrada_1')
    entrada_2 = TextField('entrada_2')
    umbral = TextField('umbral')
