import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
# print(window)
pygame.display.set_caption("Charla Pygame - Ventana")
window.fill(pygame.Color("darkgreen"))

class Main:

	while True:

		for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

		pygame.display.flip()
		# pygame.display.update()
		# pygame.display.update(args)
