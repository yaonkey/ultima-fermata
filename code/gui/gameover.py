import pygame

from settings import UI_FONT, UI_PAUSE_FONT_SIZE, TEXT_COLOR


class Gameover:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_PAUSE_FONT_SIZE)
        self.height = self.display_surface.get_size()[1]
        self.width = self.display_surface.get_size()[0]
        self.rect = pygame.Rect(0, self.height / 2, self.width, self.height, font=self.font)

    def display(self):
        title_go = self.font.render("GAME OVER", True, TEXT_COLOR)
        title_rect = title_go.get_rect(midtop=self.rect.midtop)

        restart_text = self.font.render("Restart", True, TEXT_COLOR)
        restart_rect = restart_text.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 100))

        self.display_surface.blit(title_go, title_rect)
        self.display_surface.blit(restart_text, restart_rect)
