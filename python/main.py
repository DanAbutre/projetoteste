import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 480
altura = 640
clock = pygame.time.Clock()
fps = 60

tela = pygame.display.set_mode((largura, altura))
titulo = pygame.display.set_caption("War Space PY")

bg1 = pygame.image.load("python/estrada.jpg")
bg = pygame.transform.scale(bg1, (largura, altura))

nave1_1 = pygame.image.load("python/moto.png")
nave_1 = pygame.transform.scale(nave1_1, (300, 300))

def fundo():
    tela.blit(bg, (0, 0))


class Nave_amiga(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = nave_1
        self.rect = self.image.get_rect()
        self.rect.center =[x ,y]


    def update(self):
        speed = 2
        key = pygame.key.get_pressed()
        if key[K_a]:
            self.rect.x -= speed
        elif key[K_d]:
            self.rect.x += speed
        elif key[K_w]:
            self.rect.y -= speed
        elif key[K_s]:
            self.rect.y += speed
            

nave = Nave_amiga(int(largura / 2), altura - 100)

nave_grupo = pygame.sprite.Group()

nave_grupo.add(nave)

run = True
while run:
    clock.tick(fps)
    fundo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()

    nave.update()
    nave_grupo.draw(tela)

    pygame.display.flip()

pygame.quit()
