from network import Network
import pygame, sys
from settings import *
from level import Level

# pygame setup
pygame.init()
pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
screen = pygame.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))
screen.fill((255, 255, 255))
crt_shader = Graphic_engine(screen=screen, style=2, VIRTUAL_RES=VIRTUAL_RES)
pygame.display.set_caption("Client")
network = Network()
clock = pygame.time.Clock()
level = Level(level_data=no_p_level_map, surface=screen)
# player = network.get_pos()
# print(player)
# level.visible_sprites.add(player)
# level.player.add(player)

print("START")
while True:
    # player2 = network.send(player)
    # level.visible_sprites.add(player2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                crt_shader.change_shader()

    level.run()

    crt_shader()
    clock.tick(60)