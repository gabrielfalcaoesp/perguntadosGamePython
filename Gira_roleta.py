import pygame
import sys
import random

pygame.init()

temas = {
    1: 'Geografia', 
    2: 'História',
    3: 'Esportes',
    4: 'Entretenimento'
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
    },

    {
        "tema": "Esportes",
        "pergunta": "Quem é o maior artilheiro da história das Copas do Mundo?",
        "alternativas": ["A) Pelé", "B) Ronaldo", "C) Miroslav Klose", "D) Lionel Messi"],
        "resposta_correta": "C"
    },

    {
        "tema": "Entretenimento",
        "pergunta": "Qual foi o primeiro filme da franquia 'Star Wars' a ser lançado?",
        "alternativas": ["A) A Ameaça Fantasma", "B) O Império Contra-Ataca", "C) Uma Nova Esperança", "D) O Retorno de Jedi"],
        "resposta_correta": "C"
    }
]

# Variáveis de estado do jogo
tema = 1
pontuacao = 0
vidas = 3
girando = False
angulo = 0
novoAngulo = 0

# Dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Carrega a imagem da roleta e botão
roleta = pygame.image.load(r'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Game Python\\roleta.png')
roleta = pygame.transform.scale(roleta, (275, 275))  

botao_girar = pygame.image.load(r'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Game Python\\botao.png')
botao_girar = pygame.transform.scale(botao_girar, (90, 100))  

clock = pygame.time.Clock()

# Função para exibir uma pergunta
def CriarPergunta(temaEscolhido):
    perguntasDoTema = [p for p in perguntas if p['tema'] == temaEscolhido]
    perguntaEscolhida = random.choice(perguntasDoTema)
    
    print(f"Tema: {perguntaEscolhida['tema']}")
    print(perguntaEscolhida["pergunta"])
    for alternativa in perguntaEscolhida["alternativas"]:
        print(alternativa)
    
    resposta = input("Digite a resposta correta: ").upper()  # Lógica de input precisa ser adaptada para Pygame
    if resposta == perguntaEscolhida["resposta_correta"]:
        print("Você acertou!")
        return 10  # Pontuação ganha
    else:
        print("Resposta incorreta!")
        return -1  # Perde uma vida

# Função para girar a roleta
def GirarRoleta(efetuarGiro):
    global angulo, novoAngulo, tema, girando
    if efetuarGiro and not girando:
        girando = True
        tema = random.randint(1, 4)
        novoAngulo = angulo + (360 + (tema * 90))
    
    if girando:
        if angulo < novoAngulo:
            angulo += 5
        else:
            girando = False
            CriarPergunta(temas[tema])

    roleta_rotacionada = pygame.transform.rotate(roleta, angulo)
    novo_centro = roleta_rotacionada.get_rect(center=(largura_tela // 2, altura_tela // 2))
    return roleta_rotacionada, novo_centro

# Função para inserir a roleta na tela
def InserirRoleta(roleta_rotacionada, rect_rotacionado):
    tela.blit(roleta_rotacionada, rect_rotacionado)

# Função para inserir o botão girar
def InserirBotaoGirar():
    largura_botao, altura_botao = botao_girar.get_size()
    x = (largura_tela - largura_botao) // 2
    y = (altura_tela - altura_botao) // 2 + 150
    tela.blit(botao_girar, (x, y))
    return (x, y, largura_botao, altura_botao)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                botao_x, botao_y, largura_botao, altura_botao = InserirBotaoGirar()
                if (botao_x <= mouse_x <= botao_x + largura_botao) and (botao_y <= mouse_y <= botao_y + altura_botao):
                    GirarRoleta(True)

    tela.fill((255, 255, 255))
    roleta_rotacionada, novo_centro = GirarRoleta(False)
    InserirRoleta(roleta_rotacionada, novo_centro)
    InserirBotaoGirar()

    pygame.display.flip()
    clock.tick(60)
