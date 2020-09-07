from stiri_v_vrsto_model import *
from bottle import route
import bottle
polje = Polje()

@route('/')
def index():
    # Napiše na vrhu, kdo je na vrsti oz. kdo je zmagal
    if polje.zmaga != 0:
        if polje.zmaga == 1:
            sporocilo = 'RDEČI igralec je zmagal!'
        else:
            sporocilo = 'RUMENI igralec je zmagal!'
    elif polje.igralec == 1:
        sporocilo = 'Na vrsti je RDEČI igralec'
    else:
        sporocilo = 'Na vrsti je RUMENI igralec'

    # Pokaže polje
    out = ''
    for y in range(POLJE_VISINA - 1, -1, -1):
        for x in range(POLJE_SIRINA):
            zeton = polje.polje[x][y]
            if zeton == 1:
                out += '<div class="prostor zeton1"></div>'
            elif zeton == 2:
                out += '<div class="prostor zeton2"></div>'
            else:
                out += '<div class="prostor"></div>'

    return bottle.template('index.tpl', polje=out, sporocilo=sporocilo)


@route('/igraj/<x>')
def igraj(x):
    x = int(x)

    if polje.zmaga:
        polje.resetiraj()

    polje.dodaj_zeton(x)

    return index()

@route('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='views/img/')

bottle.run(host='localhost', port=8080)
