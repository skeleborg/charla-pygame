import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
pygame.display.set_caption("Charla Pygame")
window.fill(pygame.Color("darkgreen"))

class Samus(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.transform.scale2x(pygame.image.load('./samus.png').convert_alpha())
        # sin escalar: (0, 0, 25, 48)
        self.image = self.sprite_sheet.subsurface((0, 0, 50, 96))
        self.rect = self.image.get_rect()
        self.rect.center = (window.get_width() / 2, window.get_height() / 2)

    def update(self):
        pass


samus = Samus()
samus_sprite_group = pygame.sprite.GroupSingle()
samus_sprite_group.add(samus)

class Main:

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        samus_sprite_group.draw(window)
        pygame.display.flip()


