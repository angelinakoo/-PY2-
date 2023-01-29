
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: идентификатор книги
        :param name: Название книги
        :param pages:  Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор доожен быть типа int")
        if not isinstance(name, str):
            raise TypeError("Название доожно быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц доожно быть типа int")
        if id_ < 0:
            raise ValueError("Идентификатор не может быть отрицательным числом")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
