import pygame
import sys

pygame.init()

window = pygame.display.set_mode([600, 300])
pygame.display.set_caption("Charla Pygame")
window.fill(pygame.Color("darkgreen"))
clock = pygame.time.Clock()
fps = pygame.font.SysFont("Arial", 30)


class Samus(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.transform.scale2x(pygame.image.load('./samus.png'))
        self.animation_sheet = self.sprite_sheet.subsurface((480, 700, 380, 300))
        self.image = self.sprite_sheet.subsurface((0, 0, 50, 96))
        self.rect = self.image.get_rect()
        self.rect.center = (100, window.get_height() / 2)

        self.current_hframe = 0
        self.current_vframe = 0
        # Total de frames = 10
        self.hframes = 4
        self.vframes = 3
        self.frame_width = self.animation_sheet.get_width() / self.hframes
        self.frame_height = self.animation_sheet.get_height() / self.vframes

        self.animate = False

    def update(self):
        if self.current_hframe < self.hframes - 1:
            self.current_hframe += 1
        if self.current_vframe < self.vframes - 1 and self.current_hframe == self.hframes - 1:
            self.current_vframe += 1
            self.current_hframe = 0
        if self.current_hframe == self.hframes / 2 - 1 and self.current_vframe == self.vframes - 1:
            self.current_hframe = 0
            self.current_vframe = 0

        self.image = self.animation_sheet.subsurface((self.frame_width * self.current_hframe, self.frame_height * self.current_vframe, self.frame_width, self.frame_height))
        self.rect.x = (self.rect.x + 15) % window.get_width()

samus = Samus()
single_sprite_group = pygame.sprite.GroupSingle()
single_sprite_group.add(samus)


class Main:

    while True:
        for event in pygame.event.get():

            key = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if key[pygame.K_RIGHT]:
                    single_sprite_group.sprite.animate = True

            if event.type == pygame.KEYUP:
                if single_sprite_group.sprite.animate:
                    single_sprite_group.sprite.animate = False
                    single_sprite_group.sprite.image = single_sprite_group.sprite.sprite_sheet.subsurface((0, 0, 50, 96))

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(pygame.Color("darkgreen"))
        if single_sprite_group.sprite.animate:
            single_sprite_group.sprite.update()
        single_sprite_group.draw(window)
        fps_counter = fps.render("FPS: " + str(int(clock.get_fps())), True, pygame.Color('white'))
        window.blit(fps_counter, (10, 0))

        pygame.display.flip()
        clock.tick(15)
