import pyttsx3
import random
import time

tabela_periodica = {
    "Linha 1": {
        "Coluna 1": {"numero": 5, "simbolo": "B", "nome": "Boro"},
        "Coluna 2": {"numero": 6, "simbolo": "C", "nome": "Carbono"},
        "Coluna 3": {"numero": 7, "simbolo": "N", "nome": "Nitrogênio"},
        "Coluna 4": {"numero": 8, "simbolo": "O", "nome": "Oxigênio"},
    },
    "Linha 2": {
        "Coluna 1": {"numero": 13, "simbolo": "Al", "nome": "Alumínio"},
        "Coluna 2": {"numero": 14, "simbolo": "Si", "nome": "Silício"},
        "Coluna 3": {"numero": 15, "simbolo": "P", "nome": "Fósforo"},
        "Coluna 4": {"numero": 16, "simbolo": "S", "nome": "Enxofre"},
    },
    "Linha 3": {
        "Coluna 1": {"numero": 31, "simbolo": "Ga", "nome": "Gálio"},
        "Coluna 2": {"numero": 32, "simbolo": "Ge", "nome": "Germânio"},
        "Coluna 3": {"numero": 33, "simbolo": "As", "nome": "Arsênio"},
        "Coluna 4": {"numero": 34, "simbolo": "Se", "nome": "Selênio"},
    },
    "Linha 4": {
        "Coluna 1": {"numero": 49, "simbolo": "In", "nome": "Índio"},
        "Coluna 2": {"numero": 50, "simbolo": "Sn", "nome": "Estanho"},
        "Coluna 3": {"numero": 51, "simbolo": "Sb", "nome": "Antimônio"},
        "Coluna 4": {"numero": 52, "simbolo": "Te", "nome": "Telúrio"},
    },
    "Linha 5": {
        "Coluna 1": {"numero": 81, "simbolo": "Tl", "nome": "Tálio"},
        "Coluna 2": {"numero": 82, "simbolo": "Pb", "nome": "Chumbo"},
        "Coluna 3": {"numero": 83, "simbolo": "Bi", "nome": "Bismuto"},
        "Coluna 4": {"numero": 84, "simbolo": "Po", "nome": "Polônio"},
    },
    "Linha 6": {
        "Coluna 1": {"numero": 113, "simbolo": "Nh", "nome": "Nihônio"},
        "Coluna 2": {"numero": 114, "simbolo": "Fl", "nome": "Fleróvio"},
        "Coluna 3": {"numero": 115, "simbolo": "Mc", "nome": "Moscóvio"},
        "Coluna 4": {"numero": 116, "simbolo": "Lv", "nome": "Livermório"},
    },
}


engine = pyttsx3.init()

# Configurar a voz para português
voices = engine.getProperty('voices')
for voice in voices:
    if "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break


engine.setProperty('rate', 180)


def falar(texto):
    print (texto)
    engine.say(texto)
    engine.runAndWait()


for i in range(15):
    nColuna=random.randint(1, 4)
    nLinha=random.randint(1, 6)
    coluna = f"Coluna {nColuna}"
    linha = f"Linha {nLinha}"
    tipoPergunta=random.randint(1, 5)
    if tipoPergunta==1:
        pergunta = f"Qual o elemento da {linha} e {coluna}"
        falar(pergunta)
        time.sleep(6)
        falar(tabela_periodica[linha][coluna]["nome"])
    if tipoPergunta==2:
        direcoes=[]
        if nColuna>1:
            direcoes.append('esquerda')
        if nColuna<4:
            direcoes.append('direita')
        if nLinha>1:
            direcoes.append('acima')
        if nLinha<6:
            direcoes.append('abaixo')
        direcaoPergunta=random.choice(direcoes)
        pergunta = f"Quais os elementos à {direcaoPergunta} do {tabela_periodica[linha][coluna]['nome']} ?"
        falar(pergunta)
        resposta=""

        if direcaoPergunta=='esquerda':
            for i in range(1,nColuna):
                resposta+=f" {tabela_periodica[linha]['Coluna '+str(i)]['nome']},"
        if direcaoPergunta=='direita':
            for i in range(nColuna+1,5):
                resposta+=f"{tabela_periodica[linha]['Coluna '+str(i)]['nome']},"
        if direcaoPergunta=='acima':
            for i in range(1,nLinha):
                resposta+=f"{tabela_periodica['Linha '+str(i)][coluna]['nome']},"
        if direcaoPergunta=='abaixo':
            for i in range(nLinha+1,7):
                resposta+=f"{tabela_periodica['Linha '+str(i)][coluna]['nome']},"

        time.sleep(6)
        falar(resposta)
        time.sleep(2)

    if tipoPergunta==3:
        pergunta = f"Responda, em ordem, os elementos da coluna  {nColuna}"
        falar(pergunta)
        time.sleep(6)
        resposta = ""
        for i in range(1, 7):
            resposta += f" {tabela_periodica['Linha '+str(i)][coluna]['nome']},"
        time.sleep(2)
        falar(resposta)

    if tipoPergunta==4:
        pergunta = f"Responda, em ordem, os elementos da linha  {nLinha}"
        falar(pergunta)
        time.sleep(6)
        resposta = ""
        for i in range(1, 5):
            resposta += f" {tabela_periodica[linha]['Coluna '+str(i)]['nome']},"
        time.sleep(2)
        falar(resposta)


    if tipoPergunta==5:
        pergunta = f"Qual o elemento de número atômico {tabela_periodica[linha][coluna]['numero']}"
        falar(pergunta)
        time.sleep(6)
        falar(tabela_periodica[linha][coluna]["nome"])
        time.sleep(2)







