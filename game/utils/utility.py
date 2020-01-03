import pygame
from game.utils.constans import FONT_NAME, FONT_SIZE, WHITE


def load_img(path):
    img = pygame.image.load(path)
    if img.get_alpha is None:
        img = img.convert()
    else:
        img = img.convert_alpha()

    return img, img.get_rect()


def draw_text(surf, text, x, y):
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
