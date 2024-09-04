import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

screen = None
clock  = None
dt     = None

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame_init = pygame.init()
    print(f"pygame loaded {pygame_init[0]} out of {pygame_init[0] + pygame_init[1]} modules successfully.")

    inputtable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    CircleShape.containers = (updateable, drawable)
    Player.containers = (inputtable, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    

    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2
    )

    asteroid_field = AsteroidField()

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
        k = pygame.key.get_pressed()
        for sprite in inputtable:
            sprite.input(dt, k)

        # Update
        for sprite in updateable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game over!")
                exit()

        # Draw
        screen.fill(SCREEN_BACKGROUND_COLOR)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.update()

        # post
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
