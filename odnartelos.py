import pyttsx3
import random
import time

palavras = [
    "Amar", "Boleto", "Descer", "Estimulo", "Garganta",
    "Ilha", "Justiça", "Leitura", "Máximo", "Numérico",
    "Outrora", "Pálido", "Recesso", "Quociente", "Super"
]

engine = pyttsx3.init()

# Configurar a voz para português
voices = engine.getProperty('voices')
for voice in voices:
    if "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Configurar velocidade (opcional)
engine.setProperty('rate', 180)


def falar(texto):
    print (texto)
    engine.say(texto)
    engine.runAndWait()


def soletrar_palavra(palavra):
    falar(f"A palavra é: {palavra}")
    time.sleep(10)
    for letra in reversed(palavra):
        falar(letra)
        time.sleep(0.1)

# Loop principal
palavras_disponiveis = palavras.copy()
while palavras_disponiveis:
    falar (f"Faltam {len(palavras_disponiveis)} palacras")
    palavra_sorteada = random.choice(palavras_disponiveis)
    soletrar_palavra(palavra_sorteada)
    palavras_disponiveis.remove(palavra_sorteada)

falar("Todas as palavras foram sorteadas e soletradas!")
