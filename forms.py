from wtforms import Form
from wtforms import TextField

class NeuronaForm(Form):
    e1 = TextField('e1')
    p1 = TextField('p1')
    e2 = TextField('e2')
    p2 = TextField('p2')
    e3 = TextField('e3')
    p3 = TextField('p3')
    u = TextField('u')
