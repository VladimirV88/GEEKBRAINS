"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


# класс одежда
class Clothes:
    def __init__(self, name):
        self.name = name


# класс пальто
class Coat:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # затраты на одежду
    @property
    def cloth_cost(self):
        self.__cloth_cost = self.size / 6.5 + 0.5
        return round(self.__cloth_cost, 2)

    def real_cloth_cost(self):
        return f"Расход ткани на '{self.name}' составляет {self.cloth_cost}м2"


# класс костюм
class Suit:
    def __init__(self, name, height):
        self.name = name
        self.size = height

    # затраты на одежду
    @property
    def cloth_cost(self):
        self.__cloth_cost = self.size * 2 + 0.3
        return round(self.__cloth_cost, 2)

    def real_cloth_cost(self):
        return f"Расход ткани на '{self.name}' составляет {self.cloth_cost}м2"


v = float(input("Введите размер пальто (например, 56): "))
h = float(input("Введите Ваш рост в сантиметрах (например, 180): ")) / 100

coat = Coat("Пальто", v)
suit = Suit("Костюм", h)

print(f'Вы указали размер пальто равным {v}, и рост {h}м')
print(coat.real_cloth_cost())
print(suit.real_cloth_cost())
