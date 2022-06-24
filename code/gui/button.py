import pygame
from code.settings import UI_FONT, UI_PAUSE_FONT_SIZE, TEXT_COLOR, UI_BG_COLOR, BUTTON_BG_CLICKED, TEXT_COLOR_CLICKED


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos):
        self.x, self.y = pos
        self.font = pygame.font.SysFont(UI_FONT, TEXT_COLOR)
        self.change_text(text, UI_BG_COLOR)

    def change_text(self, text):
        """Change the text whe you click"""
        self.text = self.font.render(text, True, TEXT_COLOR_CLICKED)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(BUTTON_BG_CLICKED)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback  )
