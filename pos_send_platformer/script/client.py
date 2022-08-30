from network import Network
import pygame, sys
from settings import *
from level import Level
from player import Player

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
# level.player.add
player = Player((100, 100),
[level.visible_sprites,
level.player],
level.create_jump_or_run_particles)
player2 = Player((100, 100),
[level.visible_sprites],
level.create_jump_or_run_particles)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tuple):
    return str(tuple[0]) + "," + str(tuple[1])

print("START")
while True:
    player2_pos = read_pos(network.send(make_pos((player.rect.x, player.rect.y))))
    player2.rect.x = player2_pos[0]
    player2.rect.y = player2_pos[1]

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