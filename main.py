import pygame

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20
fps = 60
pos_y = 30

class PlacePlay:
    # создание поля
    def __init__(self):
        self.pole = []
        self.pole = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]
        self.pos_y2 = pos_y

    def render(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         (250, 30, 350, 700), 1)

    def drop_item(self):
        if pos_y % 35 == 0:
            self.pos_y2 = pos_y
        pygame.draw.rect(screen, (255, 255, 255),
                     (285, self.pos_y2, 35, 35))

clock = pygame.time.Clock()
running = True
play = PlacePlay()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    play.render()
    play.drop_item()
    pygame.display.flip()
    if pos_y < 694:
        pos_y += 100 // fps
    clock.tick(fps)


    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
