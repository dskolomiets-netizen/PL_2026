#ФУНКЦИИИИИИ
import pygame
from pygame.draw import*
from pygame.draw import circle

pygame.init()
screen = pygame.display.set_mode((300, 200))

rect(screen, (200, 200, 200), (0, 0, 300, 200))
circle(screen, (255, 255, 0), (150, 100), 50)
rect(screen, (0, 0, 0), (120, 120, 60, 10))
def eye(x, y):
    circle(screen, (255, 0, 0), (x+120, 80), 15-y)
    circle(screen, (0, 0, 0), (x+120, 80), 5)
eye(0, 0)
eye(60, 5)
polygon(screen, (0, 0, 0), [(200, 50), (155,70),(155, 65), (200, 45)], 10)
polygon(screen, (0, 0, 0), [(100, 50), (135,70),(135, 65), (100, 45)], 10)
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

