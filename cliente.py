import json 
import aiohttp
import asyncio

URL_ARTILHEIROS = "http://localhost:5001/"
ARTILHEIROS_IS_ALIVE = URL_ARTILHEIROS + "isalive/"
ARTILHEIROS = URL_ARTILHEIROS + "artilheiros/"
URL_PARTIDAS = "http://localhost:5002/"
PARTIDAS_IS_ALIVE = URL_PARTIDAS + "isalive/"
PARTIDAS = URL_PARTIDAS + "partidas/"
URL_RESULTADOS = "http://localhost:5003/"
RESULTADOS_IS_ALIVE = URL_RESULTADOS + "isalive/"
RESULTADOS = URL_RESULTADOS + "resultados/"

async def acessar(url):
    dados = None

    async with aiohttp.ClientSession() as sessao:
        async with sessao.get(url) as resposta:
            dados = await resposta.text()

    return dados

async def artilheiros_is_alive():
    alive = False

    if await acessar(ARTILHEIROS_IS_ALIVE) == "yes":
        alive = True

    return alive

async def get_artilheiros():
    dados = await acessar(ARTILHEIROS)
    artilheiros = json.loads(dados)
    return artilheiros

def imprimir_artilheiros(artilheiros):
    print("ARTILHEIROS DO SANTOS NA TEMPORADA: ")
    for i in range(len(artilheiros)):
        print("Jogador:", artilheiros[i]['nome'], "Gols marcados:", artilheiros[i]['gols'])

async def acessar_artilheiros():
    while True:
        if await artilheiros_is_alive():
            artilheiros = await get_artilheiros()
            imprimir_artilheiros(artilheiros)
        else:
            print("servico indisponivel")

        await asyncio.sleep(3) 

async def partidas_is_alive():
    alive = False

    if await acessar(PARTIDAS_IS_ALIVE) == "yes":
        alive = True

    return alive

async def get_partidas():
    dados = await acessar(PARTIDAS)
    partidas = json.loads(dados)
    return partidas

def imprimir_partidas(partidas):
    print("PROXIMAS PARTIDAS DO SANTOS: ")
    for i in range(len(partidas)):
        print("Partida:", partidas[i]['jogo'])
        print("Campeonato:", partidas[i]['campeonato'])
        print("Data:", partidas[i]['dia'])
        print("Hora:", partidas[i]['horario'])

async def acessar_partidas():
    while True:
        if await partidas_is_alive():
            partidas = await get_partidas()
            imprimir_partidas(partidas)
        else:
            print("servico indisponivel")

        await asyncio.sleep(3)

async def resultados_is_alive():
    alive = False

    if await acessar(RESULTADOS_IS_ALIVE) == "yes":
        alive = True

    return alive

async def get_resultados():
    dados = await acessar(RESULTADOS)
    resultados = json.loads(dados)
    return resultados

def imprimir_resultados(resultados):
    print("ULTIMOS RESULTADOS DO SANTOS: ")
    for i in range(len(resultados)):
        print("Partida:", resultados[i]['resultado'])
        print("Campeonato:", resultados[i]['campeonato'])
        print("Data:", resultados[i]['dia'])

async def acessar_resultados():
    while True:
        if await resultados_is_alive():
            resultados = await get_resultados()
            imprimir_resultados(resultados)
        else:
            print("servico indisponivel")

        await asyncio.sleep(3)

async def executar():
    await asyncio.gather(acessar_artilheiros(), acessar_partidas(), acessar_resultados())

if __name__ == "__main__":
    asyncio.run(executar())