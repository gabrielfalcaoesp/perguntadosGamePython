import random

temas = {
    1: 'Geografia', 
    2: "História"
}

perguntas = [
    {
        "tema": "Geografia",
        "pergunta": "Qual é o animal mais rápido do mundo?",
        "alternativas": ["A) Guepardo", "B) Falcão Peregrino", "C) Leão", "D) Cavalo"],
        "resposta_correta": "B"
    },

    {
        "tema": "Geografia",
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "alternativas": ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"],
        "resposta_correta": "C"
    }, 

    {
        "tema": "História",
        "pergunta": "Em que ano a Primeira Guerra Mundial começou?",
        "alternativas": ["A) 1914", "B) 1918", "C) 1939", "D) 1945"],
        "resposta_correta": "A"
    }
]

pontuacao = 0
vidas = 3

temaEscolhido = temas[random.randint(1, len(temas))]

perguntasDoTema = []
for pergunta in perguntas:
    if pergunta['tema'] == temaEscolhido:
        perguntasDoTema.append(pergunta)

while vidas > 0:
    perguntaEscolhida = random.randint(0, len(perguntasDoTema)-1)
    print(f"Tema: {temaEscolhido} - Pergunta: {perguntaEscolhida}")
    perguntaAtual = perguntasDoTema[perguntaEscolhida]

    print(perguntaAtual.get("pergunta"))
    for alternativa in perguntaAtual.get("alternativas"):
        print(alternativa)
    resposta = input ("Digite a resposta correta: ").upper()
    if(resposta == perguntaAtual.get("resposta_correta")):
        print("Você acertou!")
        pontuacao += 10
    else:
        vidas -= 1
        print(f"Opa, você perdeu uma vida!, restam apenas: {vidas}")
print(f"Sua pontuação total foi: {pontuacao}")
