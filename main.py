import pygame
from constants import *

screen = None
clock  = None
dt     = None

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame_init = pygame.init()
    print(f"pygame loaded {pygame_init[0]} out of {pygame_init[0] + pygame_init[1]} modules successfully.")

    clock = pygame.time.Clock()
    dt = 0
    print("Game clock initialized")
    
    print("Creating game screen...")
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Screen created successfully")
    except Exception as e:
        print(f"Error creating screen: {e}")
    
    while True:
        # pre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Input

        # Update

        # Draw
        screen.fill(SCREEN_BACKGROUND_COLOR)
        pygame.display.update()

        # post
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
