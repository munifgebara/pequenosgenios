import pyttsx3
import random
import time

def calcula(numero1, operador, numero2):
    if operador == 1:
        return numero1+numero2
    elif operador == 2:
        return numero1-numero2
    elif operador == 4:
        return numero1*numero2
    elif operador == 3:
        return numero1//numero2
    else:
        raise ValueError("Número inválido! Deve estar entre 1 e 4.")

def operacao(operador):
    if operador == 1:
        return "mais"
    elif operador == 2:
        return "menos"
    elif operador == 4:
        return "vezes"
    elif operador == 3:
        return "dividido por"
    else:
        raise ValueError("Número inválido! Deve estar entre 1 e 4.")

def gerar_divisor_aleatorio(N):
    # Gera todos os divisores válidos entre 2 e 9
    divisores = [X for X in range(2, 10) if N % X == 0]

    # Verifica se há divisores disponíveis
    if not divisores:
        return 1

    # Escolhe um divisor ao acaso
    return random.choice(divisores)


engine = pyttsx3.init()

# Configurar a voz para português
voices = engine.getProperty('voices')
for voice in voices:
    if "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Configurar velocidade (opcional)
engine.setProperty('rate', 200)

numero = random.randint(10, 50)

for i in range(10):
    if numero > 400:
       operador = random.randint(1, 3)
    else:
       operador = random.randint(1, 4)

    if operador == 1:
        operando =  random.randint(2, 99)
    if operador == 2:
        operando =  random.randint(2, numero)
    if operador == 4:
        operando = random.randint(2, 9)
    if operador == 3:
        operando = gerar_divisor_aleatorio(numero)

    texto = f"{numero} {operacao(operador)} {operando}"
    print (f"{i} -> {texto}")
    engine.say(texto)
    engine.runAndWait()
    numero=calcula(numero,operador,operando)
    time.sleep(3+2*operador)
    print(numero)
    engine.say(f"{numero}")
    engine.runAndWait()


