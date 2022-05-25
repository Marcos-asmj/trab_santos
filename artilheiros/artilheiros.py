from flask import Flask
from flask import jsonify

app = Flask(__name__)

IS_ALIVE = "yes"
ARTILHEIROS = [
    {
        "id": 1,
        "nome": 'Marcos Leonardo',
        "gols": 8,
    },
    {
        "id": 2,
        "nome": 'Ricardo Goulart',
        "gols": 4,
    },
    {
        "id": 3,
        "nome": 'Vinicius Zanocelo',
        "gols": 4,
    },
    {
        "id": 4,
        "nome": 'Leo Baptistao',
        "gols": 4,
    },
    {
        "id": 5,
        "nome": 'Brayan Angulo',
        "gols": 3,
    },
    {
        "id": 6,
        "nome": 'Rwan Seco',
        "gols": 3,
    },
    {
        "id": 7,
        "nome": 'Marcos Guilherme',
        "gols": 2,
    },
    {
        "id": 8,
        "nome": 'Madson',
        "gols": 2,
    },
    {
        "id": 9,
        "nome": 'Eduardo Gabriel',
        "gols": 1,
    },
    {
        "id": 10,
        "nome": 'Lucas Braga',
        "gols": 1,
    },
    {
        "id": 11,
        "nome": 'Kaiky',
        "gols": 1,
    },
    {
        "id": 12,
        "nome": 'Lucas Barbosa',
        "gols": 1,
    },
    {
        "id": 13,
        "nome": 'Angelo Gabriel',
        "gols": 1,
    },
    {
        "id": 14,
        "nome": 'Rodrigo Fernandez',
        "gols": 1,
    },
    {
        "id": 15,
        "nome": 'Jhojan Julio',
        "gols": 1,
    },
]

@app.route("/isalive/")
def is_alive():
    return IS_ALIVE

@app.route("/artilheiros/")
def get_artilheiros():
    artilheiros = jsonify(
        ARTILHEIROS
    )
    return artilheiros

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        debug = True
    )