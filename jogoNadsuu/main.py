import pygame
import sys

# Inicializa o pygame
pygame.init()
screen_width, screen_height = 640, 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nadsuu Adventure")
clock = pygame.time.Clock()

# Carrega as imagens dos fundos
bg1 = pygame.image.load("camada1.png").convert()       # camada 1 (mais distante)
bg2 = pygame.image.load("camada2.png").convert_alpha()   # camada 2
bg3 = pygame.image.load("camada3.png").convert_alpha()   # camada 3
bg4 = pygame.image.load("camada4.png").convert_alpha()   # camada 4
bg5 = pygame.image.load("camada5.png").convert_alpha()   # camada 5
bg6 = pygame.image.load("camada6.png").convert_alpha()   # camada 6
bg7 = pygame.image.load("camada7.png").convert_alpha()   # camada 7
bg8 = pygame.image.load("camada8.png").convert_alpha()   # camada 8 (mais próxima)

# Posições iniciais para cada camada
x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = 0

# Velocidades de deslocamento (quanto menor, mais distante parece)
speed1 = 0.5   # mais distante
speed2 = 0.8
speed3 = 1.0
speed4 = 1.5
speed5 = 2.0
speed6 = 2.5
speed7 = 3.0
speed8 = 3.5   # mais próxima

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza as posições (movendo para a esquerda)
    x1 -= speed1
    x2 -= speed2
    x3 -= speed3
    x4 -= speed4
    x5 -= speed5
    x6 -= speed6
    x7 -= speed7
    x8 -= speed8

    # Reseta a posição para criar o loop infinito
    if x1 <= -bg1.get_width():
        x1 = 0
    if x2 <= -bg2.get_width():
        x2 = 0
    if x3 <= -bg3.get_width():
        x3 = 0
    if x4 <= -bg4.get_width():
        x4 = 0
    if x5 <= -bg5.get_width():
        x5 = 0
    if x6 <= -bg6.get_width():
        x6 = 0
    if x7 <= -bg7.get_width():
        x7 = 0
    if x8 <= -bg8.get_width():
        x8 = 0

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha cada camada duas vezes para garantir continuidade
    screen.blit(bg1, (x1, 0))
    screen.blit(bg1, (x1 + bg1.get_width(), 0))
    
    screen.blit(bg2, (x2, 0))
    screen.blit(bg2, (x2 + bg2.get_width(), 0))
    
    screen.blit(bg3, (x3, 0))
    screen.blit(bg3, (x3 + bg3.get_width(), 0))
    
    screen.blit(bg4, (x4, 0))
    screen.blit(bg4, (x4 + bg4.get_width(), 0))
    
    screen.blit(bg5, (x5, 0))
    screen.blit(bg5, (x5 + bg5.get_width(), 0))
    
    screen.blit(bg6, (x6, 0))
    screen.blit(bg6, (x6 + bg6.get_width(), 0))
    
    screen.blit(bg7, (x7, 0))
    screen.blit(bg7, (x7 + bg7.get_width(), 0))
    
    screen.blit(bg8, (x8, 0))
    screen.blit(bg8, (x8 + bg8.get_width(), 0))
    
    # Atualiza a tela e define 60 FPS
    pygame.display.flip()
    clock.tick(60)
