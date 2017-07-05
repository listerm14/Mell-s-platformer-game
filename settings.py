# game options/settings
import pygame as pg
import random
from os import path


snd_dir = path.join(path.dirname(__file__), 'smd')


TITLE = "Jumpy!"
WIDTH = 480
HEIGHT = 600
FPS = 65

FONT_NAME = 'comic sans'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"


# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.25
PLAYER_GRAV = 0.8
PLAYER_JUMP = -27

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = (74, 45, 115)
BGCOLOR2 = (32, 0, 27)
BGCOLOR3 = (43 , 48, 70)
SPRITE = (131, 61, 0)

