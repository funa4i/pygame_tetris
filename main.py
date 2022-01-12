import pygame
import numpy as np
import klass_figur
import copy
import tetris_random
import random

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
x_col = 10
y_col = 20
fps = 60
pos_y_global = 0
flag = True
kvadrat_figura = klass_figur.Kub()
liniya_figura = klass_figur.Pryamaya()
stupen_1_figura = klass_figur.StupenVLevo()
stupen_2_figura = klass_figur.StupenVPravo()
g_russka_figura = klass_figur.GPravil()
g_ne_russka_figura = klass_figur.GNePravil()
t_figura = klass_figur.TObraz()
instr_rand = tetris_random.FigurePool(random.randint(1, 100000000000))
pull_figur = []
for i in range(5):
    pull_figur.append(instr_rand.get_figure())


class PlacePlay:
    def __init__(self):
        self.pole = np.zeros((20, 10), dtype=np.int16)
        self.mest_polosh = []

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
        flag = True
        pos_y_global = 0
        # -------------------------
        if num == 1:
            self.mest_polosh = copy.deepcopy(kvadrat_figura.cord)
        elif num == 2:
            liniya_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(liniya_figura.cord)
        elif num == 3:
            stupen_1_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(stupen_1_figura.cord)
        elif num == 4:
            stupen_2_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(stupen_2_figura.cord)
        elif num == 5:
            g_russka_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(g_russka_figura.cord)
        elif num == 6:
            g_ne_russka_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(g_ne_russka_figura.cord)
        elif num == 7:
            t_figura.return_to_start_cord()
            self.mest_polosh = copy.copy(t_figura.cord)
        for i in self.mest_polosh:
            self.pole[i[0]][i[1]] = 1

    def drop_item(self, x_change=0, y_change=1):
        locl_flag = True
        locl_flag_2 = True
        "Очень стршная проеверка 1"
        for qw in self.mest_polosh:  # Проверка на возможность упасть
            vr_sp = [qw[0] + 1, qw[1]]
            if (self.pole[qw[0] + 1][qw[1]] == 1) and not vr_sp in self.mest_polosh:
                locl_flag = False
        "Очень стршная проеверка 2"
        if x_change != 0:
            for i in range(len(self.mest_polosh)):  # Проверка на возможность движение
                vrem = (self.mest_polosh[i][-1] + x_change) % 10
                print(vrem)
                chek = [self.mest_polosh[i][0], vrem]
                print(chek)
                if self.pole[chek[0]][chek[-1]] == 1 and not chek in self.mest_polosh:
                    locl_flag_2 = False
        if locl_flag:
            for i in self.mest_polosh:
                self.pole[i[0]][i[1]] = 0
            if self.lower_cord(self.mest_polosh) != 19:
                for i in range(len(self.mest_polosh)):
                    self.mest_polosh[i][0] += y_change
            if locl_flag_2:
                for i in range(len(self.mest_polosh)):
                    vrem = (self.mest_polosh[i][-1] + x_change) % 10
                    self.mest_polosh[i][-1] = vrem
            for i in self.mest_polosh:
                self.pole[i[0]][i[1]] = 1
        else:
            play.spawn_figure(take_new_figure())

    def lower_cord(self, sp):
        g = set()
        for i in sp:
            g.add(i[0])
        g = list(g)
        return max(g)


def take_new_figure():
    pull_figur.append(instr_rand.get_figure())
    znach = pull_figur[0]
    del pull_figur[0]
    return znach


clock = pygame.time.Clock()
running = True
play = PlacePlay()
play.spawn_figure(take_new_figure())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if flag:
                if event.key == pygame.K_a:
                    play.drop_item(-1, 0)
                if event.key == pygame.K_d:
                    play.drop_item(1, 0)
                if event.key == pygame.K_s:
                    h = 19 - play.lower_cord(play.mest_polosh)
                    play.drop_item(0, h)
                    play.spawn_figure(take_new_figure())
    screen.fill((0, 0, 0))
    play.render()
    pygame.display.flip()
    if play.lower_cord(play.mest_polosh) != 19:
        pos_y_global += (100 // fps) * 4
        if pos_y_global % 35 == 0:
            print(pos_y_global)
            play.drop_item(0, 1)
    else:
        flag = False
        play.spawn_figure(take_new_figure())
    clock.tick(fps)
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Иницилизация игры')
