import pygame

class Ball:
    def __init__(self, x, y, xvel, yvel, acceleration, e_loss, height, width, radius, screen, color):
      self.xPos = x
      self.yPos = y
      self.xVel = xvel
      self.yVel = yvel
      self.acc = acceleration
      self.loss = e_loss
      self.HEIGHT = height
      self.WIDTH = width
      self.RADIUS = radius
      self.screen = screen
      self.color = color

    def update_ball(self):
      self.yPos += self.yVel
      self.xPos += self.xVel
      self.yVel += self.acc

      if self.yPos > self.HEIGHT - self.RADIUS:
        self.yPos = self.HEIGHT - self.RADIUS
        self.yVel = -self.yVel * self.loss

      if self.xPos > self.WIDTH - self.RADIUS or self.xPos < self.RADIUS:
        self.xVel = -self.xVel

    def draw(self):
      self.update_ball()
      pygame.draw.circle(self.screen, self.color, [int(self.xPos), int(self.yPos)], self.RADIUS, 0)
