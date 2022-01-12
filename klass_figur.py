import copy


class Kub:
    def __init__(self):
        self.CORD_NACH = [[0, 4], [0, 5], [1, 4], [1, 5]]
        self.cord = [[0, 4], [0, 5], [1, 4], [1, 5]]


class Pryamaya:
    def __init__(self):
        self.CORD_NACH = [[0, 3], [0, 4], [0, 5], [0, 6]]
        self.cord = copy.deepcopy(self.CORD_NACH)

    def return_to_start_cord(self):
        self.cord = copy.deepcopy(self.CORD_NACH)


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
