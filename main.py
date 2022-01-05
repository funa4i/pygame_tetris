import pygame
import numpy as np

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20
fps = 60
pos_y_global = 0
flag = True


class PlacePlay:
    def __init__(self):
        self.pole = np.zeros((20, 10), dtype=np.int16)
        self.x = 4
        self.y = 0


    def render(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         (250, 35, 350, 700), 1)
        for i in range(20):
            for j in range(10):
                if self.pole[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (250 + j * 35, 35 + i * 35, 35, 35))


    def spawn_figure(self, num=0):
        global flag, pos_y_global
        self.x = 4
        self.y = 0
        self.pole[self.y][self.x] = 1
        flag = True
        pos_y_global = 0

    def drop_item(self, x_change=0, y_change=1):
        self.pole[self.y][self.x] = 0
        if self.y != 19:
            self.y += y_change
            print(self.y)
        self.x += x_change
        self.pole[self.y][self.x] = 1

class Kub:
    def __init__(self):
        self.nachaln_cord = [[0, 4], [0, 5], [1, 4], [1, 5]] # Не изменяять не прикаком уловии
        self.cord = [[0, 4], [0, 5], [1, 4], [1, 5]]

    def lowest_cord(self):
        g = set()
        for i in self.cord:
            g.add(i[-1])
        g = min(list(g))
        return g



clock = pygame.time.Clock()
running = True
play = PlacePlay()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if flag:
                if event.key == pygame.K_a:
                    if play.x != 0:
                        play.drop_item(-1, 0)
                if event.key == pygame.K_d:
                    if play.x != 9:
                        play.drop_item(1, 0)
                if event.key == pygame.K_s:
                    h = 19 - play.y
                    play.drop_item(0, h)
                    play.spawn_figure()
    screen.fill((0, 0, 0))
    play.render()
    pygame.display.flip()
    if pos_y_global < 755:
        pos_y_global += 100 // fps
        if pos_y_global % 35 == 0:
            print(pos_y_global)
            play.drop_item(0, 1)
    else:
        flag = False
        play.spawn_figure()
    clock.tick(fps)

    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
