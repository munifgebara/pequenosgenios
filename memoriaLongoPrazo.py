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

# Exemplo de acesso:
print(tabela_periodica["Linha 1"]["Coluna 3"])  # {'numero': 7, 'simbolo': 'N', 'nome': 'Nitrogênio'}
