import sys
import time
import pygame

pygame.init()

width, height = 600, 337
size = width, height
tela = pygame.display.set_mode((600, 337))
pygame.display.set_caption("main")

imagem_fundo = pygame.image.load("fundo.png")
boneco = pygame.image.load("Hurt.png")
boneco.set_colorkey((255, 255, 255))
bonecorect = boneco.get_rect()
bonecorect.y = 190
bonecorect.x = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bonecorect.x -= 5
        if bonecorect.left < 0:
            bonecorect.left = 0
    if keys[pygame.K_RIGHT]:
        bonecorect.x += 5
        if bonecorect.right > 640:
            bonecorect.right = 640
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(boneco, bonecorect)
    pygame.display.flip()
    time.sleep(0.015)
