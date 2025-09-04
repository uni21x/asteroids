import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        from constants import ASTEROID_MIN_RADIUS
        import random

        # Kill this asteroid
        self.kill()

        # If it's too small, don't create new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate random split angle
        split_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        vel1 = self.velocity.rotate(split_angle)
        vel2 = self.velocity.rotate(-split_angle)

        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids with increased speeds
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = vel1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = vel2 * 1.2