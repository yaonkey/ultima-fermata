import pygame

from settings import UI_FONT, UI_PAUSE_FONT_SIZE, TEXT_COLOR


class Pause:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_PAUSE_FONT_SIZE)
        self.height = self.display_surface.get_size()[1]
        self.width = self.display_surface.get_size()[0]
        self.rect = pygame.Rect(0, self.height / 2, self.width, self.height, font=self.font)

    def display(self):
        title_pause = self.font.render("PAUSE", True, TEXT_COLOR)
        title_rect = title_pause.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))
        self.display_surface.blit(title_pause, title_rect)
