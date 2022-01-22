import copy


class Kub:
    def __init__(self):
        self.CORD_NACH = [[0, 4], [0, 5], [1, 4], [1, 5]]
        self.cord = [[0, 4], [0, 5], [1, 4], [1, 5]]


class Pryamaya:
    def __init__(self):
        self.CORD_NACH = [[0, 3], [0, 4], [0, 5], [0, 6]]
        self.cord = copy.deepcopy(self.CORD_NACH)
        self.vert_pol = [[-2, 2], [-1, 1], [0, 0], [1, -1]]
        self.gor_pol = [[2, -2], [1, -1], [0, 0], [-1, 1]]

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)

    def povovrot(self, pole, polos_povor, pov):
        polos_povor_vn = (abs(polos_povor + pov)) % 2
        print(self.cord)
        if polos_povor_vn == 1:
            vrem = iszm_cord(self.cord, self.vert_pol)
            if check_next_cord(pole, vrem, self.cord):
                for i in range(len(self.cord)):
                    self.cord[i] = vrem[i]
        else:
            vrem = iszm_cord(self.cord, self.gor_pol)
            if check_next_cord(pole, vrem, self.cord):
                for i in range(len(self.cord)):
                    self.cord[i] = vrem[i]


class StupenVLevo:
    def __init__(self):
        self.CORD_NACH = [[0, 3], [0, 4], [1, 4], [1, 5]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


class StupenVPravo:
    def __init__(self):
        self.CORD_NACH = [[1, 3], [0, 4], [1, 4], [0, 5]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


class GPravil:
    def __init__(self):
        self.CORD_NACH = [[0, 4], [1, 4], [1, 5], [1, 6]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


class GNePravil:
    def __init__(self):
        self.CORD_NACH = [[1, 3], [1, 4], [0, 5], [1, 5]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


class TObraz:
    def __init__(self):
        self.CORD_NACH = [[1, 3], [0, 4], [1, 4], [1, 5]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


def max_cord(sp):
    g = set()
    for i in sp:
        g.add(i[0])
    g = list(g)
    return min(g)


def iszm_cord(last, ch):
    for i in range(len(last)):
        print(last, ch)
        l, l2 = last[i][0] + ch[i][0], last[i][-1] + ch[i][-1]
        last[i][0] = l
        last[i][-1] = l2
    print("________________________________________________________________")
    return last


def check_next_cord(pole: list, new_cord: list, old_cord):
    for i in range(len(new_cord)):
        if pole[[i][0]][[i][-1]] != 0 and new_cord[[i][0]][[i][-1]] not in old_cord:
            return False
    return True
