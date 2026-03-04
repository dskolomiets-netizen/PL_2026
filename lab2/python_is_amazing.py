import pygame
from pygame.draw import*
from pygame.draw import circle

pygame.init()
screen = pygame.display.set_mode((300, 200))
#плакат
rect(screen, (0, 255, 0), (0, 0, 300, 20))
font = pygame.font.SysFont("Times New Roman", 20, bold=True)
text = font.render("PYTHON is AMAZING", True, (0, 0, 0))
screen.blit(text, (50, 0))
#arms
polygon(screen, (210, 180, 160), [(20, 20),(100, 160),(120, 150),(30, 20)])
polygon(screen, (210, 180, 160), [(280, 20),(180, 160),(200, 150),(290, 20)])

#body
circle(screen, (210, 100, 0), (150, 200), 60)

#cap
circle(screen, (255, 0, 255), (150, 60), 40)
font = pygame.font.SysFont("Times New Roman", 10, bold=True)
text = font.render("tractor", True, (255, 255, 255))
screen.blit(text, (135, 30))
rect(screen, (255, 0, 255), (150, 60, 50, 5))
rect(screen, (0, 0, 0), (150, 60, 50, 5), 1)

#face
circle(screen, (210, 180, 160), (150, 100), 50)
polygon(screen, (255, 0, 0), [(120, 120), (180, 120), (150, 140)])
polygon(screen, (50, 0, 0), [(145, 100), (155, 100), (150, 110)])
def eye(x):
    circle(screen, (100, 100, 200), (x+130, 90), 10)
    circle(screen, (0, 0, 0), (x+130, 90), 5)
eye(0)
eye(50)
#cap part
rect(screen, (255, 0, 255), (110, 55, 80, 10))
rect(screen, (0, 0, 0), (110, 55, 80, 10),1)

#sleves
polygon(screen, (210, 100, 0), [(120, 150), (100, 170), (90, 170), (120, 130), (130, 140)])
polygon(screen, (0, 0, 0), [(120, 150), (100, 170), (90, 170), (120, 130), (130, 140)], 1)
polygon(screen, (210, 100, 0), [(180, 150), (210, 170), (220, 170), (180, 130), (190, 140)])
polygon(screen, (0, 0, 0), [(180, 150), (210, 170), (220, 170), (180, 130), (190, 140)], 1)
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

