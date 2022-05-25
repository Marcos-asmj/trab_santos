from flask import Flask
from flask import jsonify

app = Flask(__name__)

IS_ALIVE = "no"
RESULTADOS = [
    {
        "id": 1,
        "resultado": 'Goias 1x0 Santos',
        "dia": '15/05/2022',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 2,
        "resultado": 'Santos 3x0 Coritiba',
        "dia": '12/05/2022',
        "campeonato": 'Copa do Brasil'
    },
    {
        "id": 3,
        "resultado": 'Santos 4x1 Cuiaba',
        "dia": '08/05/2022',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 4,
        "resultado": 'Universidad Catolica 0x1 Santos',
        "dia": '05/05/2022',
        "campeonato": 'Copa Sul-Americana'
    },
    {
        "id": 5,
        "resultado": 'Sao Paulo 2x1 Santos',
        "dia": '02/05/2022',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 6,
        "resultado": 'Union La Calera 1x1 Santos',
        "dia": '28/04/2022',
        "campeonato": 'Copa Sul-Americana'
    }
]

@app.route("/isalive/")
def is_alive():
    return IS_ALIVE

@app.route("/resultados/")
def get_resultados():
    resultados = jsonify(
        RESULTADOS
    )
    return resultados

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        debug = True
    )