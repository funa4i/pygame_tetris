import pygame

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)


class place_play:
    # создание поля
    def __init__(self):
        pass



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
