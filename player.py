import pygame
import os
from settings import WIDTH, HEIGHT, BLACK, IMAGE_DIR

class Player(pygame.sprite.Sprite):
    def __init__(self, balas_group):  # Recibe el grupo de balas
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, 'player.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.balas_group = balas_group  # Guardamos referencia al grupo de balas

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def disparar(self):
        bala = Balas(self.rect.centerx, self.rect.top)
        self.balas_group.add(bala)  # Agregamos la bala al grupo

class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Imagen temporal
        self.image.fill((255, 255, 255))  # Color blanco para la bala
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= 10  # Mover la bala hacia arriba
        if self.rect.bottom < 0:
            self.kill()  # Eliminar la bala cuando salga de la pantalla
