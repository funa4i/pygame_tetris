import pygame

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20


class PlacePlay:
    # создание поля
    def __init__(self):
        pass

    def render(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         (250, 30, 350, 700), 1)


running = True
play = PlacePlay()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    play.render()
    pygame.display.flip()

    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
