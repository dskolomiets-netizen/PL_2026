import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Здесь мы будем рисовать
def background(surface, color, width, height):
    '''
    фон
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    width, height - размеры поля
    '''
    rect(surface, color, (0, 0, width, height))

def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_eyes(surface, x, y, size):
    '''
    рисует глаз
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    '''
    circle(surface, (0, 0, 0), (x, y), size // 2)

def draw_hare(surface, x, y, width, height, color):
  '''
  Рисует зайца на экране.
  surface - объект pygame.Surface
  x, y - координаты левого верхнего угла изображения
  width, height - ширина и высота изобажения
  color - цвет, заданный в формате, подходящем для pygame.Color
  '''

  body_width = width // 2
  body_height = height // 2
  body_y = y + body_height // 2
  draw_body(surface, x, body_y, body_width, body_height, color)

  head_size = height // 4
  draw_head(surface, x, y - head_size // 2, head_size, color)

  ear_height = height // 3
  ear_y = y - height // 2 + ear_height // 2
  for ear_x in (x - head_size // 4, x + head_size // 4):
      draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)

  leg_height = height // 16
  leg_y = y + height // 2 - leg_height // 2
  leg_y2 = y - height // 2 + leg_height // 2
  leg_y3 = y - height // 128 + leg_height
  for leg_x in (x - width // 5, x + width // 5):
      draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)
      draw_leg(surface, leg_x, leg_y2, width // 4, leg_height, color)
      draw_leg(surface, leg_x, leg_y3, width // 2, leg_height, color)
  eye_size = height // 8
  eye_y = y - height // 8
  for eye_x in (x - width // 4, x + width // 4):
      draw_eyes(surface, eye_x, eye_y, eye_size)
background(screen,(255, 200, 200),400, 400)
draw_hare(screen, 200, 200, 200, 400, (200, 200, 200))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
