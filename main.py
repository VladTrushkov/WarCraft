from units import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    speed = 0
    running = True

    all_sprites = pygame.sprite.Group()
    #all_sprites_2 = pygame.sprite.Group()
    active_sprite = None
    #sprite = pygame.sprite.Sprite(all_sprites)
    """
    image_cursor = load_image(r"sprites\human\startpoint.png")
    cursor = pygame.sprite.Sprite(all_sprites_2)
    cursor.image = pygame.transform.scale(image_cursor, (CELL_SIZE, CELL_SIZE))
    cursor.rect = cursor.image.get_rect()
    """

    #image = load_image(r"sprites\human\units\peasant.png")
    #sprite.image = image
    #sprite.image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    #cut_sheet(image, 1, 1)
    #sprite.image = frames[3]
    #sprite.rect = sprite.image.get_rect()

    setka = Map()
    for _ in range(1):
        peasant = Peasant(all_sprites)
        peasant_2 = Peasant(all_sprites)
        setka.set_object(3, 3, peasant)
        setka.set_object(1, 2, peasant_2)

    for obj in all_sprites:
        obj.rect.x, obj.rect.y = setka.get_coordinates(obj)
    while running:
        SCREEN.fill((0, 0, 0))
        setka.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = event.pos
                i, j = setka.get_cells(x_mouse, y_mouse)
                if event.button == 1:
                    obj = setka.get_object(i, j)
                    active_sprite = obj if obj else None
                elif event.button == 3:
                    if active_sprite:
                        setka.set_object(i, j, active_sprite)
                print(obj)
                if obj:
                    obj.rect.x, obj.rect.y = setka.get_coordinates(obj)
                setka.print_map()
                """
                cursor.rect.x = x_mouse
                cursor.rect.y = y_mouse
                all_sprites_2.update()
                """
        #peasant.rect.x, peasant.rect.y = setka.get_coordinates(peasant)
        #sprite.rect.x = 72
        #sprite.rect.y = 72

        #speed += clock.tick() / 100
        #i = int(speed % 5)
        #sprite.image = frames[i]
        all_sprites.draw(SCREEN)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
