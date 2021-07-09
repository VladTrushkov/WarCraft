from settings import *


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
    sprite = pygame.transform.scale(sprite, (CELL_SIZE, CELL_SIZE))
    return sprite


def get_sprites(image_sprites, row, column, row_count, column_count, reverse=False):
    rect = pygame.Rect(0, 0, 72, 72)
    frames = []
    for j in range(row, row + row_count):
        for i in range(column, column + column_count):
            frame_location = (rect.w * i, rect.h * j)
            frame = image_sprites.subsurface(pygame.Rect(frame_location, rect.size))
            if reverse:
                frame = pygame.transform.flip(frame, True, False)
            frames.append(frame)
    return frames


def sprites_peasant_move_up(image_file):
    return get_sprites(image_file, 0, 0, 5, 1)


def sprites_peasant_move_down(image_file):
    return get_sprites(image_file, 0, 4, 5, 1)


def sprites_peasant_move_right(image_file):
    return get_sprites(image_file, 0, 2, 5, 1)


def sprites_peasant_move_left(image_file):
    return get_sprites(image_file, 0, 2, 5, 1, reverse=True)


def sprites_peasant_move_up_right(image_file):
    return get_sprites(image_file, 0, 1, 5, 1)


def sprites_peasant_move_up_left(image_file):
    return get_sprites(image_file, 0, 1, 5, 1, reverse=True)


def sprites_peasant_move_down_right(image_file):
    return get_sprites(image_file, 0, 3, 5, 1)


def sprites_peasant_move_down_left(image_file):
    return get_sprites(image_file, 0, 3, 5, 1, reverse=True)
