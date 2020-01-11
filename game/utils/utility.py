"""
utils
"""
import pygame
from game.utils.constans import FONT_NAME, FONT_SIZE, WHITE


def load_img(path):
    """
    load image form path
    :param path:
    :return:
    """
    img = pygame.image.load(path)
    if img.get_alpha is None:
        img = img.convert()
    else:
        img = img.convert_alpha()

    return img, img.get_rect()


def draw_text(surf, text, pos_x, pos_y, size=FONT_SIZE):
    """
    function draw text on screen
    :param surf:
    :param text:
    :param pos_x:
    :param pos_y:
    :param size:
    :return:
    """
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (pos_x, pos_y)
    surf.blit(text_surface, text_rect)
