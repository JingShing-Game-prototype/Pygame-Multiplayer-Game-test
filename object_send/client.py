import pygame
from network import Network
# remove make pos and read pos function. Use pickle to send object.

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    network = Network()
    player = network.get_pos()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2 = network.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        redraw_window(win, player, player2)

print("START")
main()