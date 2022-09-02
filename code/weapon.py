import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        # graphic
        full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement
        match direction:
            case 'right':
                self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
            case 'left':
                self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
            case 'down':
                self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))
            case 'up':
                self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))
