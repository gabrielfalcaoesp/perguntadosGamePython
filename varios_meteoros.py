import pygame
import sys
import random

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo com Meteoros')

branco = (255, 255, 255)
vermelho = (255, 0, 0)

x = largura_tela // 2
y = altura_tela // 2

meteoros = [{'x': random.randint(0, largura_tela - 50), 'y': random.randint(-100, -50)} for _ in range(5)]

velocidade_meteoro = 7
velocidadeImg = 5

imagem_meteoro = ""
imagem_jogador = ""

clock = pygame.time.Clock()

def colisao(obj1, obj2, meteoro_x, meteoro_y):
    rect1 = obj1.get_rect(topleft=(x, y))
    rect2 = obj2.get_rect(topleft=(meteoro_x, meteoro_y))
    return rect1.colliderect(rect2)

def CriarJogador():
    global imagem_jogador
    imagem_jogador = pygame.image.load(r'C:\Users\gabri\OneDrive\Área de Trabalho\Game Python\corinthians.png')
    imagem_jogador = pygame.transform.scale(imagem_jogador, (75, 100))
    tela.blit(imagem_jogador, (x, y))

def MoverJogador():
    global x, y
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x > 0:
        x -= velocidadeImg
    if teclas[pygame.K_RIGHT] and x < largura_tela - 75:
        x += velocidadeImg
    if teclas[pygame.K_UP] and y > 0:
        y -= velocidadeImg
    if teclas[pygame.K_DOWN] and y < altura_tela - 100:
        y += velocidadeImg

def CriarMeteoros():
    global imagem_meteoro
    imagem_meteoro = pygame.Surface((50, 50))
    imagem_meteoro.fill(vermelho)
    
    for meteoro in meteoros:
        tela.blit(imagem_meteoro, (meteoro['x'], meteoro['y']))

def MoverMeteoros():
    for meteoro in meteoros:
        meteoro['y'] += velocidade_meteoro

def ResetarMeteoros():
    for meteoro in meteoros:
        if meteoro['y'] > altura_tela:
            meteoro['y'] = -50
            meteoro['x'] = random.randint(0, largura_tela - 50)

while True:
    tela.fill(branco)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    CriarJogador()
    MoverJogador()
    CriarMeteoros()
    MoverMeteoros()
    ResetarMeteoros()

    for meteoro in meteoros:
        if colisao(imagem_jogador, imagem_meteoro, meteoro['x'], meteoro['y']):
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
