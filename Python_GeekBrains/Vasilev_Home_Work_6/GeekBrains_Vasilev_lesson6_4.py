"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car(object):
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.color.title()} {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.color.title()} {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.color.title()} {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Автомобиль {self.color.title()} {self.name}. Скорость движения: {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color.title()} {self.name}, вы превысили скорость!!!")
        else:
            print(f"{self.color.title()} {self.name}, скорость движения: {self.speed} км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили ограничение скорости для рабочего автомобиля!")
        else:
            print(f"Скорость движения: {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


t_one = TownCar(60, "красный", "Citroen")
print(f"Автомобиль: {t_one.color}, {t_one.name}, {t_one.speed} км/ч, полиция = {t_one.is_police}")

t_two = TownCar(80, "черный", "Volvo")
print(f"Автомобиль: {t_two.color}, {t_two.name}, {t_two.speed} км/ч, полиция = {t_two.is_police}")

w = WorkCar(50, "оранжевый", "КамАЗ")
print(f"Автомобиль: {w.color}, {w.name}, {w.speed} км/ч, полиция = {w.is_police}")

s = SportCar(250, "красно-желтый", "Porche")
print(f"Автомобиль: {s.color}, {s.name}, {s.speed} км/ч, полиция = {s.is_police}")

p = PoliceCar(90, "бело-голубой", "BMW")
print(f"Автомобиль: {p.color}, {p.name}, {p.speed} км/ч, полиция = {p.is_police}")

# Все тронулись
t_one.go()
t_two.go()
w.go()
s.go()
p.go()

# смотрим скорость
t_one.show_speed()
t_two.show_speed()
w.show_speed()
s.show_speed()
p.show_speed()

# кто-то поворачивает
t_one.turn("направо")
t_two.turn("налево")
p.turn("налево")

# полиция останавливает одного из нарушителей :)
t_two.stop()
p.stop()
