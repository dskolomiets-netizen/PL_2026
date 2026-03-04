import pygame
from pygame.draw import*
from pygame.draw import circle

pygame.init()
screen = pygame.display.set_mode((1200, 200))
#плакат
rect(screen, (0, 255, 0), (0, 0, 1200, 20))
font = pygame.font.SysFont("arial", 20, bold=True)
text = font.render("PYTHON is amazingly amazingly amazingly amazingly amazingly AMAZING", True, (0, 0, 0))
screen.blit(text, (300, 0))

def dude(x, c):
    # arms
    polygon(screen, (210, 180, 160), [(x+20, 20),(x+100, 160),(x+120, 150),(x+30, 20)])
    polygon(screen, (210, 180, 160), [(x+280, 20),(x+180, 160),(x+200, 150),(x+290, 20)])

    #body
    circle(screen, (210-c, 100, 0), (x+150, 200), 60)

    #cap
    circle(screen, (255-c, 0, 255), (x+150, 60), 40)
    rect(screen, (255-c, 0, 255), (x+150, 60, 50, 5))
    rect(screen, (0, 0, 0), (x+150, 60, 50, 5), 1)

    #face
    circle(screen, (210, 180, 160), (x+150, 100), 50)
    polygon(screen, (255, 0, 0), [(x+120, 120), (x+180, 120), (x+150, 140)])
    polygon(screen, (50, 0, 0), [(x+145, 100), (x+155, 100), (x+150, 110)])
    circle(screen, (100, 100, 200), (x+130, 90), 10)
    circle(screen, (0, 0, 0), (x+130, 90), 5)
    circle(screen, (100, 100, 200), (x+165, 90), 10)
    circle(screen, (0, 0, 0), (x+165, 90), 5)

    #cap part
    rect(screen, (255-c, 0, 255), (x+110, 55, 80, 10))
    rect(screen, (0, 0, 0), (x+110, 55, 80, 10),1)

    #sleves
    polygon(screen, (210-c, 100, 0), [(x+120, 150), (x+100, 170), (x+90, 170), (x+120, 130), (x+130, 140)])
    polygon(screen, (0, 0, 0), [(x+120, 150), (x+100, 170), (x+90, 170), (x+120, 130), (x+130, 140)], 1)
    polygon(screen, (210-c, 100, 0), [(x+180, 150), (x+210, 170), (x+220, 170), (x+180, 130), (x+190, 140)])
    polygon(screen, (0, 0, 0), [(x+180, 150), (x+210, 170), (x+220, 170), (x+180, 130), (x+190, 140)], 1)
    pygame.display.update()

dude(0, 50)
dude(300, 150)
dude(600, 20)
dude(900, 200)

clock = pygame.time.Clock()
clock.tick(30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

