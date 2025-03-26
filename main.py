import pygame
import os
from settings import WIDTH, HEIGHT, IMAGE_DIR, BLACK
from player import Player
from meteor import Meteor

# Inicialización
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GALAGA')
clock = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(os.path.join(IMAGE_DIR, 'background.png')).convert()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
balas = pygame.sprite.Group()  # Grupo de balas

# Crear jugador y pasarle el grupo de balas
player = Player(balas)
all_sprites.add(player)

# Crear meteoritos
for i in range(10):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_list.add(meteor)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.disparar()  # Llamar a la función disparar

    # Actualizar los sprites
    all_sprites.update()
    balas.update()
     #COLISIONES
    for bala in balas:
        if bala.rect.y < 0:
            bala.kill()
        meteor_hit_list = pygame.sprite.spritecollide(bala, meteor_list, True)
        for meteor in meteor_hit_list:
            bala.kill()
            meteor.kill()
            # Crear un nuevo meteorito en la posición del meteorito destruido
            new_meteor = Meteor()
            all_sprites.add(new_meteor)
            meteor_list.add(new_meteor) 
            
   
           

    # Dibujar en pantalla
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))  # Dibujar fondo
    all_sprites.draw(screen)
    balas.draw(screen)  # Dibujamos las balas

    pygame.display.flip()
    clock.tick(80)  # Limitar FPS

pygame.quit()
