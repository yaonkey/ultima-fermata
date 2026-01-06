import pygame
from settings import *
from data import item_data
from helpers.inputKeys import key as ikey


class Inventory:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Load item graphics
        self.item_graphics = {}
        for name, data in item_data.items():
            self.item_graphics[name] = pygame.image.load(data['graphic']).convert_alpha()

        # selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
        self.use_time = None
        self.can_use = True

    def input(self):
        keys = pygame.key.get_pressed()

        num_items = len(self.player.inventory)

        if num_items == 0:
            return

        if self.can_move:
            if keys[ikey['right']] and self.selection_index < num_items - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[ikey['left']] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

        if keys[ikey['attack']] and self.can_use:
            self.can_use = False
            self.use_time = pygame.time.get_ticks()
            used = self.player.use_item(self.selection_index)
            if used:
                num_items -= 1
                if self.selection_index >= num_items:
                    self.selection_index = max(0, num_items - 1)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_move and self.selection_time:
            if current_time - self.selection_time >= 300:
                self.can_move = True

        if not self.can_use and self.use_time:
            if current_time - self.use_time >= 300:
                self.can_use = True

    def display(self):
        self.input()
        self.cooldowns()

        if not self.player.inventory:
            text_surf = self.font.render("No items in inventory", False, TEXT_COLOR)
            x = self.display_surface.get_size()[0] // 2
            y = self.display_surface.get_size()[1] // 2
            text_rect = text_surf.get_rect(center=(x, y))
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
            self.display_surface.blit(text_surf, text_rect)
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)
            return

        full_width = self.display_surface.get_size()[0]
        full_height = self.display_surface.get_size()[1]
        num_items = len(self.player.inventory)
        increment = full_width // (num_items + 1)
        item_width = 100
        item_height = 150

        for i, item in enumerate(self.player.inventory):
            left = (i * increment) + (increment - item_width) // 2
            top = self.display_surface.get_size()[1] // 2 - item_height // 2
            bg_rect = pygame.Rect(left, top, item_width, item_height)

            selected = (i == self.selection_index)
            bg_color = UPGRADE_BG_COLOR_SELECTED if selected else UI_BG_COLOR
            pygame.draw.rect(self.display_surface, bg_color, bg_rect)
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 4)

            # Draw graphic
            item_key = item['type'] + '_potion'
            if item_key in self.item_graphics:
                graphic = self.item_graphics[item_key]
                graphic_rect = graphic.get_rect(center=(bg_rect.centerx, bg_rect.top + 60))
                self.display_surface.blit(graphic, graphic_rect)

            # Draw name
            name = item['type'].capitalize() + " Potion"
            name_surf = self.font.render(name, False, TEXT_COLOR)
            name_rect = name_surf.get_rect(midbottom=(bg_rect.centerx, bg_rect.bottom - 10))
            self.display_surface.blit(name_surf, name_rect)
