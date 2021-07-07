from units import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    running = True

    all_sprites = pygame.sprite.Group()
    #all_sprites_2 = pygame.sprite.Group()
    active_sprite = None
    """
    image_cursor = load_image(r"sprites\human\startpoint.png")
    cursor = pygame.sprite.Sprite(all_sprites_2)
    cursor.image = pygame.transform.scale(image_cursor, (CELL_SIZE, CELL_SIZE))
    cursor.rect = cursor.image.get_rect()
    """

    image = load_image(r"sprites\human\units\peasant.png")
    cut_sheet(image, 1, 1)

    setka = Map()
    for _ in range(1):
        peasant = Peasant(all_sprites, 3, 3)
        peasant_2 = Peasant(all_sprites, 1, 2)
        setka.set_object(peasant)
        setka.set_object(peasant_2)

    for obj in all_sprites:
        obj.rect.x, obj.rect.y = setka.get_coordinates(obj)

    MYEVENTTYPE = 30
    pygame.time.set_timer(MYEVENTTYPE, 500)
    while running:
        SCREEN.fill((0, 0, 0))
        setka.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = event.pos
                i_pos, j_pos = setka.get_cells(x_mouse, y_mouse)
                if event.button == 1:
                    obj = setka.get_object(i_pos, j_pos)
                    active_sprite = obj if obj else None
                elif event.button == 3:
                    if active_sprite:
                        active_sprite.set_new_position(i_pos, j_pos)
                print(obj)
                setka.print_map()
                """
                cursor.rect.x = x_mouse
                cursor.rect.y = y_mouse
                all_sprites_2.update()
                """
            if event.type == MYEVENTTYPE:
                for obj in all_sprites:
                    obj.move()
                    setka.set_object(obj)
                    obj.rect.x, obj.rect.y = setka.get_coordinates(obj)

        clock.tick(10)
        all_sprites.update()
        all_sprites.draw(SCREEN)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
