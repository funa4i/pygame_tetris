import random as rand


class FigurePool:
    """Рандом основанный на иссушении пула фигур с поддержкой выбора сида (если таковой задан)"""
    def __init__(self, seed=None):
        self.pool = [i + 1 for i in range(7) for _ in range(5)]  # создаем список из 35 фигур нумерация с 1
        self.seed = seed
        rand.seed(seed, version=2)

    def get_figure(self, debug=False):
        exhausted_figure = None
        figures_min = 5
        for i in range(7):  # Ищем иссушеную фигуру
            figure_counter = self.pool.count(i + 1)
            if figure_counter < figures_min:
                exhausted_figure = i + 1
                figures_min = figure_counter
        figure = rand.choice(self.pool)  # Выбираем рандомную фигуру для того что бы ее вытащить из пула
        self.pool.remove(figure)
        if exhausted_figure:  # Проверка на то есть ли вообще иссушенная фигура
            self.pool.append(exhausted_figure)
        else:
            self.pool.append(rand.choice(self.pool))  # Если не находим то просто закидываем рандомную
        self.pool.sort()  # В конце просто сортируем список для удобства
        if not debug:
            return figure
        else:
            return [exhausted_figure, figures_min, figure, self.pool]


if __name__ == '__main__':  # Дебаг рандома
    try:
        seed = int(input('Введите семя\n'))
    except ValueError:
        seed = None
    pool = FigurePool(seed)
    for i in range(10):
        debug_pool = pool.get_figure(debug=True)
        print(f'Иссушенная фигура {debug_pool[0]}\n'
              f'Количество иссушенных фигур {debug_pool[1]}\n'
              f'Фигура вытащенная рандомом {debug_pool[2]}\n'
              f'Пул после вытаскивания фигуры {debug_pool[3]}\n'
              f'Количество фигур\n'
              f'1 - {debug_pool[3].count(1)}\n'
              f'2 - {debug_pool[3].count(2)}\n'
              f'3 - {debug_pool[3].count(3)}\n'
              f'4 - {debug_pool[3].count(4)}\n'
              f'5 - {debug_pool[3].count(5)}\n'
              f'6 - {debug_pool[3].count(6)}\n'
              f'7 - {debug_pool[3].count(7)}\n')
        print("-------------------------------\n")
