# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import List


class Wheel:
    pass


class Door:
    pass


class Key:
    pass


class Auto:
    def __init__(self, wheels: List[Wheel], doors: List[Door], key: Key):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param wheels: Колеса автомобиля, задаются списком
        :param doors: Двери автомобиля, задаются списком
        :param key: Ключ от автомобиля, задается экземпляра класса Key

        Примеры:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)],
        >>> doors=[Door() for _ in range(5)], key = Key())  # инициализация экземпляра класса
        """
        self.wheels = wheels
        self.doors = doors
        self.key = key
        self.is_closed = True
        self.is_moving = False

    def open_door(self, door_num: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param door_num: Номер двери, которую необходимо открыть
        """
        pass

    def close_car(self):
        self.key.close()
        self.is_closed = True

    def start_moving(self):
        self.is_moving = True

    def stop_moving(self):
        self.is_moving = False

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
