from units import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    speed = 0
    running = True

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite(all_sprites)
    image = load_image(r"sprites\human\x_startpoint.png")
    image = load_image(r"sprites\human\units\peasant.png")
    sprite.image = image
    sprite.image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    cut_sheet(image, 1, 1)
    sprite.image = frames[3]
    sprite.rect = sprite.image.get_rect()

    for _ in range(1):
        Unit(all_sprites)

    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        sprite.rect.x = 100
        sprite.rect.y = 200
        SCREEN.fill((0, 0, 0))
        speed += clock.tick() / 60
        print(speed)
        i = int(speed % 5)
        sprite.image = frames[i]
        all_sprites.draw(SCREEN)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
