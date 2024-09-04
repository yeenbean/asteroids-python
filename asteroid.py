from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            asteroid_left_vector = self.velocity.rotate(random_angle * -1)
            asteroid_right_vector = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_left.velocity = asteroid_left_vector * 1.2
            asteroid_right.velocity = asteroid_right_vector * 1.2
