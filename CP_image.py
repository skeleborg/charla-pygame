import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
pygame.display.set_caption("Charla Pygame - Ventana")	# .convert() / .convert_alpha()
window.fill(pygame.Color("darkgreen"))

minsc = pygame.image.load('./minsc.png')


class Main:

	while True:

		for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

		window.blit(minsc, (window.get_width() / 2 - minsc.get_width() / 2, 0))
		pygame.display.flip()