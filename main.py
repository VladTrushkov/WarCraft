from settings import *
from units import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    x_pos = 0
    v = 20  # пикселей в секунду
    running = True

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = load_image(r"sprites\human\x_startpoint.png")
    sprite.rect = sprite.image.get_rect()

    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        sprite.rect.x = 100
        sprite.rect.y = 200
        #screen.fill((0, 0, 0))
        #pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        #x_pos += v * clock.tick() / 1000  # v * t в секундах
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
