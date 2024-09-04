import pygame.color

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_BACKGROUND_COLOR = pygame.Color(0, 0, 0)

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8   # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20