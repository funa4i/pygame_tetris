import pygame

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20
fps = 60
pos_y_global = 30
pos_x_global = 285

class PlacePlay:
    # создание поля
    def __init__(self):
        self.pole = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(20)]
        self.pos_y = pos_y_global
        self.pos_x = pos_x_global


    def render(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         (250, 35, 350, 700), 1)

    def drop_item(self):
        if pos_y_global % 35 == 0:
            self.pos_y = pos_y_global
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.pos_x, self.pos_y, 35, 35))

clock = pygame.time.Clock()
running = True
play = PlacePlay()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_a:
            play.pos_x -= 36
    screen.fill((0, 0, 0))
    play.render()
    play.drop_item()
    pygame.display.flip()
    if pos_y_global < 720:
        pos_y_global += 100 // fps
    clock.tick(fps)


    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
