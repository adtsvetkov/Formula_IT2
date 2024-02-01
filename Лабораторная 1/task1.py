# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import List


'''First Test Class'''
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

        Пример:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)], doors=[Door() for _ in range(5)], key = Key())  # инициализация экземпляра класса
        """
        self.wheels = wheels
        self.doors = doors
        self.key = key
        self.is_closed = True
        self.is_moving = False

    def open_door(self, door_num: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param door_num: Номер двери, которую необходимо открыть. Номер двери не может быть больше количества дверей

        Пример:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)], doors=[Door() for _ in range(5)], key = Key())
        >>> auto.open_door(1)
        """
        pass

    def close_car(self):
        """
        Переводит состояние автомобиля в закрытое с помощью ключа

        Пример:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)], doors=[Door() for _ in range(5)], key = Key())
        >>> auto.close_car()
        """
        # self.key.close()
        self.is_closed = True

    def start_moving(self):
        """
        Переводит автомобиль в состояние движения

        Пример:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)], doors=[Door() for _ in range(5)], key = Key())
        >>> auto.start_moving()
        """
        self.is_moving = True

    def stop_moving(self):
        """
        Останавливает автомобиль

        Пример:
        >>> auto = Auto(wheels=[Wheel() for _ in range(4)], doors=[Door() for _ in range(5)], key = Key())
        >>> auto.stop_moving()
        """
        self.is_moving = False


'''Second Test Class'''

class Human:
    def __init__(self, age: int, height: int, name: str):
        """
        Создание и подготовка к работе объекта "Человек"

        :param age: Возраст человека, в количестве лет
        :param height: Рост человека в см
        :param name: Имя человека

        Пример:
        >>> human = Human(age=23, height=170, name="Alex")  # инициализация экземпляра класса
        """
        self.age = age
        self.height = height
        self.name = name

    def change_name(self, new_name: str):
        """
        Изменение имени человека

        :param new_name: Новое имя человека

        Пример:
        >>> human = Human(age=23, height=170, name="Alex")# инициализация экземпляра класса
        >>> human.change_name("Viktor")
        """
        self.name = new_name

    def celebrate_birthday(self):
        """
        Празднование дня рождения человека. Изменяет возраст на 1

        Пример:
        >>> human = Human(age=23, height=170, name="Alex")# инициализация экземпляра класса
        >>> human.celebrate_birthday()
        """
        self.age += 1

    def grow(self, length: int):
        """
        Изменение роста человека

        :param length: Сколько человек прибавил/убавил в росте. Не может быть меньше (-текущий рост)

        Пример:
        >>> human = Human(age=23, height=170, name="Alex")# инициализация экземпляра класса
        >>> human.grow(5)
        """
        self.height += length


'''Third Test Class'''

class Room:
    def __init__(self, height: float, length: float, width: float, type_: str):
        """
        Создание и подготовка к работе объекта "Комната"

        :param height: Высота комнаты в см. Не может быть отрицательным
        :param length: Длина комнаты в см. Не может быть отрицательным
        :param width: Ширина комнаты в см. Не может быть отрицательным
        :param type_: Тип комнаты. Может быть только 'living', 'dining', 'bathroom' или 'toilet'

        Пример:
        >>> room = Room(height=275.0, length=603.0, width=411.0, type_="dining")  # инициализация экземпляра класса
        """
        self.height = height
        self.length = length
        self.width = width
        self.type_ = type_

    def calculate_square(self) -> float:
        """
        Подсчет площади комнаты

        :return: Площадь комнаты в квадратных сантиметрах

        Пример:
        >>> room = Room(height=275.0, length=603.0, width=411.0, type_="dining") # инициализация экземпляра класса
        >>> room.calculate_square()
        247833.0
        """
        return self.width * self.length

    def calculate_volume(self) -> float:
        """
        Подсчет объема комнаты

        :returns: Объем комнаты в кубических сантиметрах

        Пример:
        >>> room = Room(height=275.0, length=603.0, width=411.0, type_="dining") # инициализация экземпляра класса
        >>> room.calculate_volume()
        68154075.0
        """
        return self.width * self.length * self.height

    def change_room_type(self, new_type: str):
        """
        Изменение типа комнаты

        :param new_type: новый тип комнаты

        Пример:
        >>> room = Room(height=275.0, length=603.0, width=411.0, type_="dining") # инициализация экземпляра класса
        >>> room.change_room_type("living")
        """
        self.type_ = new_type

if __name__ == "__main__":
    doctest.testmod()
