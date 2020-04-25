#!/bin/python3

import pygame

from dino import Dino
from carregar_spites import carregar_imagem

tela = pygame.display.set_mode((600,300))
pygame.display.set_caption("Google Chrome Dino Game")

clock = pygame.time.Clock()
fps = 15

dino = Dino()
sprites_dino = pygame.sprite.Group(dino)

chao = carregar_imagem('chao.png')

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                dino.velocidade_x = -10
            if evento.key == pygame.K_RIGHT:
                dino.velocidade_x = 10
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                dino.stop()
    
    tela.fill((255,255,255))
    tela.blit(chao, [0,235])
    sprites_dino.update()
    sprites_dino.draw(tela)

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()