import pygame
import sys

pygame.init()

window = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Sprite animation test")
clock = pygame.time.Clock()


class Powerup(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale2x(pygame.image.load('./powerups.png'))
        # Cada powerup tiene unas dimensiones de 16x7
        self.rect = self.image.get_rect()
        self.current_frame = 0
        self.frames = 8
        self.frame_width = 32
        self.frame_height = 14

    def update(self, window):
        if self.current_frame >= self.frames - 1:
            self.current_frame = 0
        else:
            self.current_frame += 1
        new_area = pygame.Rect((self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height))
        window.blit(self.image.subsurface(new_area), (200, 200))


powerup = Powerup()
powerup_group = pygame.sprite.GroupSingle()
powerup_group.add(powerup)

class Main:    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        powerup.update(window)
        powerup_group.draw(window)
        
        pygame.display.flip()
        clock.tick(10)
