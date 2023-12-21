import pygame
from pygame.locals import QUIT
from ball import Ball

pygame.init()
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

acceleration = 0.25
loss = 0.95

b1 = Ball(100, 100, 3, 0, acceleration, loss, HEIGHT, WIDTH, 20, screen, (0, 0, 255))
b2 = Ball(500, 50, 4, 5, acceleration, loss, HEIGHT, WIDTH, 25, screen, (255, 0, 0))
b3 = Ball(200, 200, 2, 10, acceleration, loss, HEIGHT, WIDTH, 15, screen, (0, 255, 0))

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

  screen.fill((255, 255, 255))

  b1.draw()
  b2.draw()
  b3.draw()

  pygame.display.flip()
  clock.tick(60)
  
pygame.quit()
