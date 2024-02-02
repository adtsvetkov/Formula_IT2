class Book(object):
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    MIN_PAGES = 10
    MAX_PAGES = 2000

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {str(self.pages)}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={str(self.pages)})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if type(value) is not int:
            raise ValueError('Pages count must be integer, got ' + str(type(value)) + ' instead')
        elif not (PaperBook.MIN_PAGES <= value <= PaperBook.MAX_PAGES):
            raise ValueError(f'Pages count must be in [{PaperBook.MIN_PAGES}, {PaperBook.MAX_PAGES}], got ' + str(value) + ' instead')
        self._pages = value


class AudioBook(Book):
    MIN_DURATION = 10.0

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность {str(self.duration)} мин."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={str(self.duration)})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if type(value) is not float:
            raise ValueError('Book duration must be float, got ' + str(type(value)) + ' instead')
        elif AudioBook.MIN_DURATION > value:
            raise ValueError(f'Book duration must be longer than {AudioBook.MIN_DURATION}, got ' + str(value) + ' instead')
        self._duration = value
