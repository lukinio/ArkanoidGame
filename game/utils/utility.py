import pygame


def load_img(path):
    img = pygame.image.load(path)
    if img.get_alpha is None:
        img = img.convert()
    else:
        img = img.convert_alpha()

    return img, img.get_rect()
