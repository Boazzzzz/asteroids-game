import pygame
import random  
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            log_event("asteroid_split")

            random_angle = random.uniform(20, 50)
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_a = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, split_radius)

            asteroid_a.velocity = a * 1.2
            asteroid_b.velocity = b * 1.2
