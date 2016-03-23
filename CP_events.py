import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
pygame.display.set_caption("Charla Pygame")
window.fill(pygame.Color("darkgreen"))

pressed_key = pygame.font.SysFont("Arial", 30)
mensaje = ""

'''
for element in pygame.__dir__():
    print(element)
'''

class Main:

    while True:

        for event in pygame.event.get():
            print(event)

            # event_name = pygame.event.event_name(event.type)

            if event.type == pygame.KEYDOWN:
                mensaje = "Has pulsado la tecla " + str(event.__dict__["unicode"])

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(pygame.Color("darkgreen"))
        pressed_key_render = pygame.font.Font.render(pressed_key, mensaje, True, pygame.Color("white"))

        window.blit(pressed_key_render, (100, 100))
        pygame.display.flip()
