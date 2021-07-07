from settings import *
import os


frames = []


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
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
    # Модифицировать со scale??? UNIT_SIZE равен CELL_SIZE * 2
    #sprite = pygame.transform.scale(sprite, (CELL_SIZE * 2, CELL_SIZE * 2))
    return sprite


class Unit(pygame.sprite.Sprite):
    def __init__(self, group, i, j):
        super().__init__(group)
        image_file = load_image(r"sprites\human\units\peasant.png")
        self.image = get_sprite(image_file, 0, 0, UNIT_SIZE)
        self.current_i, self.current_j = i, j
        self.new_i, self.new_j = i, j
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

    def get_i(self):
        return self.i

    def get_j(self):
        return self.j

    def get_position(self):
        return self.current_i, self.current_j

    def set_position(self, i, j):
        self.current_i, self.current_j = i, j

    def set_new_position(self, i, j):
        self.new_i, self.new_j = i, j

    def move(self):
        new_i, new_j = self.new_i, self.new_j
        i, j = self.get_position()
        if i < new_i:
            i += 1
        elif i > new_i:
            i -= 1
        if j < new_j:
            j += 1
        elif j > new_j:
            j -= 1
        self.set_position(i, j)


class Peasant(Unit):
    def __init__(self, group, i, j):
        super().__init__(group, i, j)
        image_file = load_image(r"sprites\human\units\peasant.png")
        self.image = get_sprite(image_file, 0, 0, UNIT_SIZE)

    def __str__(self):
        return 'Peasant'


class Cursor(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        image_file = load_image(r"sprites\human\x_startpoint.png")
        self.image = get_sprite(image_file, 0, 0, UNIT_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Map:
    def __init__(self):
        self.map = [[None for _ in range(COUNT_CELLS)] for _ in range(COUNT_CELLS)]

    def set_object(self, obj):
        for i in range(COUNT_CELLS):
            for j in range(COUNT_CELLS):
                if self.map[i][j] == obj:
                    self.map[i][j] = None
        i_new, j_new = obj.get_position()
        self.map[i_new][j_new] = obj

    def get_object(self, i, j):
        return self.map[i][j]

    def get_coordinates(self, obj):
        for i in range(COUNT_CELLS):
            for j in range(COUNT_CELLS):
                if self.map[i][j] == obj:
                    x = (j - 0.5) * CELL_SIZE
                    y = (i - 0.5) * CELL_SIZE
                    return x, y
        return None

    def get_cells(self, x, y):
        i = y // CELL_SIZE
        j = x // CELL_SIZE
        return i, j

    def print_map(self):
        for i in range(COUNT_CELLS):
            for j in range(COUNT_CELLS):
                print(self.map[i][j], end='\t')
            print()
        print()


    def update(self):
        color = pygame.Color("white")
        for x_pos in range(CELL_SIZE, WIDTH_MAP, CELL_SIZE):
            start_pos = (x_pos, 0)
            end_pos = (x_pos, HEIGHT_MAP)
            pygame.draw.line(SCREEN, color, start_pos, end_pos, 1)
        for y_pos in range(CELL_SIZE, HEIGHT_MAP, CELL_SIZE):
            start_pos = (0, y_pos)
            end_pos = (WIDTH_MAP, y_pos)
            pygame.draw.line(SCREEN, color, start_pos, end_pos, 1)


class Button:
    pass


class Menu:
    pass
