import pygame
import numpy as np

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20
fps = 60
pos_y_global = 30


class PlacePlay:
    def __init__(self):
        self.pole = np.zeros((20, 10), dtype=np.int16)
        self.pos_y = pos_y_global
        self.a = -1
        self.b = 4
        self.pos_x = 250 + (35 * self.b)

    def render(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         (250, 35, 350, 700), 1)
        for i in range(20):
            for j in range(10):
                if self.pole[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255),
                                    (self.pos_x, self.pos_y, 35, 35))


    def drop_item(self):
        global pos_y_global, flag
        if pos_y_global % 35 == 0:
            if not flag:
                self.pole[0][4] = 1
            self.pos_y = pos_y_global
            self.a += 1
            self.pole[self.a][self.b] = 1
            self.pole[self.a - 1][self.b] = 0
            self.pole[self.a][self.b] = 0
            self.b = (self.pos_x - 250) // 35
            self.pole[self.a][self.b] = 1
            print(self.a, self.b)





clock = pygame.time.Clock()
running = True
play = PlacePlay()
flag = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if flag:
                if event.key == pygame.K_a:
                    if play.pos_x != 250:
                        play.pos_x -= 35
                if event.key == pygame.K_d:
                    if play.pos_x != 565:
                        play.pos_x += 35
                play.pole[play.a][play.b] = 1



    screen.fill((0, 0, 0))
    play.render()
    play.drop_item()
    pygame.display.flip()
    if pos_y_global < 720:
        pos_y_global += 100 // fps
    else:
        flag = False
        pos_y_global = 30
        play.a = 0
        play.b = 4
        play.pos_x = 250 + (35 * play.b)
    clock.tick(fps)

    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
