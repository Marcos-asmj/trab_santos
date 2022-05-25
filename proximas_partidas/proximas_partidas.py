from flask import Flask
from flask import jsonify

app = Flask(__name__)

IS_ALIVE = "no"
PARTIDAS = [
    {
        "id": 1,
        "jogo": 'Santos x Union La Calera',
        "dia": '18/05/2022',
        "horario": '21:30',
        "campeonato": 'Copa Sul-Americana'
    },
    {
        "id": 2,
        "jogo": 'Santos x Ceará',
        "dia": '21/05/2022',
        "horario": '18:30',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 3,
        "jogo": 'Santos x Benfield',
        "dia": '24/05/2022',
        "horario": '19:15',
        "campeonato": 'Copa Sul-Americana'
    },
    {
        "id": 4,
        "jogo": 'Santos x Palmeiras',
        "dia": '29/05/2022',
        "horario": '16:00',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 5,
        "jogo": 'Athletico-PR x Santos',
        "dia": '04/06/2022',
        "horario": '19:00',
        "campeonato": 'Campeonato Brasileiro'
    },
    {
        "id": 6,
        "jogo": 'Santos x Internacional',
        "dia": '08/06/2022',
        "horario": '21:30',
        "campeonato": 'Campeonato Brasileiro'
    }
]

@app.route("/isalive/")
def is_alive():
    return IS_ALIVE

@app.route("/partidas/")
def get_partidas():
    partidas = jsonify(
        PARTIDAS
    )
    return partidas

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        debug = True
    )