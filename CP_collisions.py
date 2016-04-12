import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
pygame.display.set_caption("Charla Pygame")
window.fill(pygame.Color("darkgreen"))
clock = pygame.time.Clock()
fps = pygame.font.SysFont("Arial", 30)

firing = False


class Samus1(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.transform.scale2x(pygame.image.load('./samus.png'))
        self.image = self.sprite_sheet.subsurface((480, 98, 90, 98))
        self.rect = self.image.get_rect()
        self.rect.center = (100, window.get_height() / 2)


class Samus2(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.transform.scale2x(pygame.image.load('./samus.png'))
        self.image = self.sprite_sheet.subsurface((0, 0, 50, 96))
        self.rect = self.image.get_rect()
        self.rect.center = (300, window.get_height() / 2)


class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./bola.png')
        self.rect = self.image.get_rect()
        self.rect.center = (145, window.get_height() / 2 - self.image.get_height() / 2)

    def update(self):
        self.rect.x += 10


samus1 = Samus1()
samus2 = Samus2()
single_sprite_group = pygame.sprite.GroupSingle()
single_sprite_group.add(samus1)
single_sprite_group2 = pygame.sprite.GroupSingle()
single_sprite_group2.add(samus2)


class Main:

    while True:
        for event in pygame.event.get():

            key = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                firing = True
                bullet = Bullet()
                single_bullet_group = pygame.sprite.GroupSingle()
                single_bullet_group.add(bullet)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(pygame.Color("darkgreen"))

        single_sprite_group.draw(window)
        single_sprite_group2.draw(window)

        if firing:
            single_bullet_group.draw(window)
            single_bullet_group.sprite.update()
            if pygame.sprite.collide_mask(samus2, bullet) and (samus2.alive() and bullet.alive()):
                bullet.kill()
                samus2.kill()
                firing = False
                print("Samus2 ha muerto.")

        fps_counter = fps.render("FPS: " + str(int(clock.get_fps())), True, pygame.Color('white'))
        window.blit(fps_counter, (10, 0))

        pygame.display.flip()
        clock.tick(15)
