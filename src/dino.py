from pygame.sprite import Sprite
import pathlib, pygame

from carregar_spites import carregar_imagem

class Dino(Sprite):

    def __init__(self, x=200, y=200):
        super(Dino, self).__init__()
     
        self.images = [
            carregar_imagem('dino1.png'),
            carregar_imagem('dino2.png'),
            carregar_imagem('dino3.png')
        ]
        self.index = 0
        self.image = self.images[self.index]

        self.velocidade_x = 0
        self.velocidade_y = 0
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 44, 47)


    def update(self):
        self.rect.move_ip(self.velocidade_x, self.velocidade_y)

        if(self.velocidade_x != 0):
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.image = self.images[self.index]

    def stop(self):
        self.velocidade_x = 0
        self.index = 0
        self.image = self.images[self.index]