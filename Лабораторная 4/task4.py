import doctest

class Human(object):
    """Базовый класс 'Человек'"""
    def __init__(self, first_name: str, last_name: str, age: int):
        """
           Создание и подготовка к работе объекта "Человек"

           :param first_name: Имя человека
           :param last_name: Фамилия человека
           :param age: Возраст человека

           Пример:
           >>> human = Human(first_name='Иван', last_name='Петров', age=20)  # инициализация экземпляра класса
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        """
           Магический метод-репрезентация основного содержания класса

           :return Строка с основной информацией о классе
           Пример:
           >>> human = Human(first_name='Иван', last_name='Петров', age=20)  # инициализация экземпляра класса
           >>> print(human)
           Человек Иван Петров, возраст 20
        """
        return f'Человек {self.first_name} {self.last_name}, возраст {str(self.age)}'

    def __repr__(self) -> str:
        """
           Магический метод, показывающий параметры для создания такого же экземпляра класса

           :return Строка с основной информацией об экземпляре
           Пример:
           >>> human = Human(first_name='Иван', last_name='Петров', age=20)  # инициализация экземпляра класса
           >>> repr(human)
           "Human(first_name='Иван', last_name='Петров', age=20)"
        """
        return f"{self.__class__.__name__}(first_name={self.first_name!r}, last_name={self.last_name!r}, age={self.age!r})"

    def get_age(self) -> int:
        """
           Возвращает возраст человека. Наследуется в дочерних классах

           :return Возраст человека в годах
           Пример:
           >>> human = Human(first_name='Иван', last_name='Петров', age=20)  # инициализация экземпляра класса
           >>> human.get_age()
           20
        """
        return self.age

    def get_additional_info(self) -> str:
        """
           Возвращает дополнительную информацию о человеке (род деятельности)

           :return Строка с указанием дополнительной информации о человеке. Содержит имя и фамилию
           Пример:
           >>> human = Human(first_name='Иван', last_name='Петров', age=20)  # инициализация экземпляра класса
           >>> human.get_additional_info()
           'Иван Петров, нет дополнительной информации'
        """
        return f'{self.first_name} {self.last_name}, нет дополнительной информации'


class Student(Human):
    """Дочерний класс 'Студент'"""
    def __init__(self, first_name: str, last_name: str, age: int, group: str):
        """
           Создание и подготовка к работе объекта "Студент"

           :param first_name: Имя студента
           :param last_name: Фамилия студента
           :param age: Возраст студента
           :param group: Номер группы

           Пример:
           >>> student = Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401')  # инициализация экземпляра класса
        """
        super().__init__(first_name, last_name, age)
        self.group = group

    def __str__(self) -> str:
        """
           Магический метод-репрезентация основного содержания класса

           :return Строка с основной информацией об объекте
           Пример:
           >>> student = Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401') # инициализация экземпляра класса
           >>> print(student)
           Студент Александр Васильев, возраст 18, номер группы 3630102/70401
        """
        return f'Студент {self.first_name} {self.last_name}, возраст {str(self.age)}, номер группы {self.group}'

    def __repr__(self) -> str:
        """
           Магический метод, показывающий параметры для создания такого же экземпляра класса

           :return Строка с основной информацией об экземпляре
           Пример:
           >>> student = Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401') # инициализация экземпляра класса
           >>> repr(student)
           "Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401')"
        """
        return f"{self.__class__.__name__}(first_name={self.first_name!r}, last_name={self.last_name!r}, age={self.age!r}, group={self.group!r})"

    def get_additional_info(self) -> str:
        """
           Возвращает дополнительную информацию о человеке, какая имеется.
           В данном случае это номер группы и род деятельности (студент).
           Поэтому метод перегружен из родительского класса

           :return Строка с указанием дополнительной информации о человеке. Содержит имя и фамилию
           Пример:
           >>> student = Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401') # инициализация экземпляра класса
           >>> student.get_additional_info()
           'Александр Васильев, студент. Группа 3630102/70401'
        """
        return f'{self.first_name} {self.last_name}, студент. Группа {self.group}'


class Teacher(Human):
    """Дочерний класс 'Преподаватель'"""
    def __init__(self, first_name: str, last_name: str, age: int, role: str):
        """
           Создание и подготовка к работе объекта "Преподаватель"

           :param first_name: Имя преподавателя
           :param last_name: Фамилия преподавателя
           :param age: Возраст преподавателя
           :param role: Должность

           Пример:
           >>> teacher = Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')  # инициализация экземпляра класса
        """
        super().__init__(first_name, last_name, age)
        self.role = role

    def __str__(self) -> str:
        """
           Магический метод-репрезентация основного содержания класса

           :return Строка с основной информацией об объекте
           Пример:
           >>> teacher = Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')  # инициализация экземпляра класса
           >>> print(teacher)
           Преподаватель Виктор Шольц, возраст 54, Декан факультета информатики
        """
        return f'Преподаватель {self.first_name} {self.last_name}, возраст {str(self.age)}, {self.role}'

    def __repr__(self) -> str:
        """
           Магический метод, показывающий параметры для создания такого же экземпляра класса

           :return Строка с основной информацией об экземпляре
           Пример:
           >>> teacher = Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')  # инициализация экземпляра класса
           >>> repr(teacher)
           "Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')"
        """
        return f"{self.__class__.__name__}(first_name={self.first_name!r}, last_name={self.last_name!r}, age={self.age!r}, role={self.role!r})"

    def get_additional_info(self) -> str:
        """
           Возвращает дополнительную информацию о человеке, какая имеется.
           В данном случае это должность и род деятельности (преподаватель).
           Поэтому метод перегружен из родительского класса

           :return Строка с указанием дополнительной информации о человеке. Содержит имя и фамилию
           Пример:
           >>> teacher = Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')  # инициализация экземпляра класса
           >>> teacher.get_additional_info()
           'Виктор Шольц, работник университета. Должность Декан факультета информатики'
        """
        return f'{self.first_name} {self.last_name}, работник университета. Должность {self.role}'

if __name__ == "__main__":
    # тест унаследованных методов
    t = Teacher(first_name='Виктор', last_name='Шольц', age=54, role='Декан факультета информатики')
    print(t.get_age())
    s = Student(first_name='Александр', last_name='Васильев', age=18, group='3630102/70401')
    print(s.get_age())
    doctest.testmod()
