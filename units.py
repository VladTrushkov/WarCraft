import pygame
from settings import *
import os
import random

SCREEN = pygame.display.set_mode(SIZE)
frames = []


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def cut_sheet(sheet, columns, rows):
    global frames
    rect = pygame.Rect(0, 0, 72, 72)
    for i in range(1):
        for j in range(5):
            frame_location = (rect.w * i, rect.h * j)
            frame = sheet.subsurface(pygame.Rect(frame_location, rect.size))
            frames.append(frame)


def get_sprite(image_sprites, i, j, size):
    """
    Получение одной спрайта из набора спрайтов
    :param image_sprites: картинка со спрайтами
    :param i: номер ряда
    :param j: номер столбца
    :param size: размер квадратика спрайта (size x size)
    :return: обрезаную картинку из спрайта
    """
    rect = pygame.Rect(0, 0, size, size)
    sprite_location = (rect.w * i, rect.h * j)
    sprite = image_sprites.subsurface(pygame.Rect(sprite_location, rect.size))
    return sprite


class Unit(pygame.sprite.Sprite):
    image_file = load_image(r"sprites\human\units\peasant.png")
    image = get_sprite(image_file, 0, 0, UNIT_SIZE)

    def __init__(self, group):
        super().__init__(group)
        self.image = Unit.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(300)
        self.rect.y = random.randrange(300)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
