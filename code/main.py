import pygame
import sys

from code.level import Level
from code.settings import *
from code.helpers.inputKeys import key as ikey


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        program_icon = pygame.image.load('../graphics/icon.png')
        pygame.display.set_icon(program_icon)
        pygame.display.set_caption('Ultima Fermata')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.wav')
        main_sound.set_volume(VOLUME)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == ikey["upgrade"]:
                        self.level.upgrade_menu()
                    elif event.key == pygame.K_ESCAPE:
                        self.level.pause_menu()
                    elif event.key == ikey["inventory"]:
                        self.level.inventory_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
