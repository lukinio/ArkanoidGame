import pygame

# Size of window
WIDTH, HEIGHT = 600, 600

# Bricks size
BRICK_WIDTH = 43
BRICK_HEIGHT = 21

# Name
DISPLAY_CAPTION = "Arkanoid"

# Basic Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# FONTS
FONT_NAME = pygame.font.match_font('arial')
FONT_SIZE = 18

# Game colors
GAME_BACKGROUND = (0, 128, 128)

# Game Speed
FPS = 60.0
BALL_SPEED = 8
PADDLE_SPEED = 8

# Game Position
TOP_OFFSET = 100
PADDLE_X, PADDLE_Y = WIDTH / 2, HEIGHT - 50
BALL_X, BALL_Y = PADDLE_X + 45, PADDLE_Y - 10

# Graphics
SRC = "game/graphics/"
PADDLE_IMG = SRC + "paddle.png"
BALL_IMG = SRC + "ball.png"
