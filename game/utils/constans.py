"""
Constans use in game
"""
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
BALL_SPEED = 7
PADDLE_SPEED = 7
BONUS_SPEED = 2
BULLET_SPEED = -10

# Game Position
TOP_OFFSET = 100
PADDLE_X, PADDLE_Y = WIDTH / 2, HEIGHT - 50
BALL_X, BALL_Y = PADDLE_X + 45, PADDLE_Y - 8

# Graphics
SRC = "game/graphics/"
BALL_IMG = SRC + "ball.png"
LIFE_IMG = SRC + "life.png"
BULLET_IMG = SRC + "bullet.png"

# Paddle state
PADDLE_IMG = SRC + "paddle.png"
PADDLE_EXPAND_IMG = SRC + "paddle_expand.png"
PADDLE_LASER_IMG = SRC + "paddle_laser.png"

# Bonus
BONUS_EXPAND_IMG = SRC + "bonus_expand.png"
BONUS_LASER_IMG = SRC + "bonus_laser.png"
BONUS_LIFE_IMG = SRC + "bonus_life.png"

# List to shuffle
LUCKY_BRICK = [True, False, False]
