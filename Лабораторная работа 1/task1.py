import doctest


class Guitar:
    def __init__(self, name_guitar: str, price_guitar: int, discount_guitar: int):
        """
        Создание и подготовка к работе объекта "Гитара"
        :param name_guitar: Название гитары
        :param price_guitar: Стоимость гитары
        :param discount_guitar: Скидка в %
        Пример:
        >>> guitar = Guitar("FENDER SQUIER", 14000, 10)  # инициализация экземпляра класса
        """
        if not isinstance(name_guitar, str):
            raise TypeError("Название доожно быть типа str")
        self.name_guitar = name_guitar

        if not isinstance(price_guitar, int):
            raise TypeError("Стоимость должна быть типа int")
        if price_guitar < 0:
            raise ValueError("Стоисмость не может быть отрицательным числом")
        self.price_guitar = price_guitar

        if not isinstance(discount_guitar, int):
            raise TypeError("Скидка должна быть типа int")
        if discount_guitar < 0:
            raise ValueError("Скидка не может быть отрицательным числом")
        if discount_guitar >= 100:
            raise ValueError("Скидка не может быть больше или равна 100%")
        self.discount_guitar = discount_guitar

    def is_here_discount(self) -> str:
        """
        Функция, которая проверяет есть ли скидка на товар
        :return: Имеется ли скидка
        Пример:
        >>> guitar = Guitar("FENDER SQUIER", 14000, 10)
        >>> guitar.is_here_discount()
        'Скидка имеется на данный продукт!'
        """
        if self.discount_guitar == 0:
            return 'Скидки нет!'
        if self.discount_guitar > 0:
            return 'Скидка имеется на данный продукт!'

    def discounted_price(self) -> float:
        """
        Функция, которая возвращает цену, учитывая скидку.
        :return: цена со скидкой
        Пример:
        >>> guitar = Guitar("FENDER SQUIER", 14000, 10)
        >>> guitar.discounted_price()
        12600.0
        """
        return self.price_guitar - self.price_guitar * self.discount_guitar / 100


guitar = Guitar("FENDER SQUIER", 14000, 10)


class Salary:
    def __init__(self, employee: str, average_salary: int, work_experience: int):
        """
        Создание и подготовка к работе объекта "Зарплата"
        :param employee: ФИО работника
        :param average_salary: средняя зарплата
        :param work_experience: стаж
        Пример:
        >>> salary = Salary("Вин Дизель", 70000, 10)  # инициализация экземпляра класса
        """
        if not isinstance(employee, str):
            raise TypeError("ФИО доожно быть типа str")
        self.employee = employee

        if not isinstance(average_salary, int):
            raise TypeError("Зарплата должна быть типа int")
        if average_salary < 0:
            raise ValueError("Зарплата не может быть отрицательным числом")
        self.average_salary = average_salary

        if not isinstance(work_experience, int):
            raise TypeError("Стаж должен быть типа int")
        if work_experience < 0:
            raise ValueError("Стаж не может быть отрицательным числом")
        self.work_experience = work_experience

    def real_salary(self) -> float:
        """
        Функция, которая возвращает реальную зарплату, получаемую работником
        При этом 1 год стажа = увеличение зарплаты на 5%
        :return: Реальная зарплата
        Пример:
        >>> salary = Salary("Вин Дизель", 70000, 10)
        >>> salary.real_salary()
        105000.0
        """
        return self.average_salary + self.average_salary * self.work_experience * 5 / 100

    def new_year_salary(self) -> int:
        """
        Функция, которая возвращает новогоднюю зарплату.
        :return: Новогодняя зарплата
        Пример:
        >>> salary = Salary("Вин Дизель", 70000, 10)
        >>> salary.new_year_salary()
        140000
        """
        return self.average_salary * 2


salary = Salary("Вин Дизель", 70000, 10)


class BuyInBookshop:
    def __init__(self, amount_books: int, current_points: int, sum_: int):
        """
        Создание и подготовка к работе объекта "Покупка в книжном магазине"
        :param amount_books: Количество книг
        :param current_points: Имеющиеся баллы
        :param sum_: Сумма покупки
        Пример:
        >>> buy_in_bookshop = BuyInBookshop(3, 25, 3200)  # инициализация экземпляра класса
        """
        if not isinstance(amount_books, int):
            raise TypeError("Количество книг должно быть типа int")
        if amount_books < 0:
            raise ValueError("Количество книг не может быть отрицательным числом")
        self.amount_books = amount_books

        if not isinstance(current_points, int):
            raise TypeError("Имеющиеся баллы должны быть типа int")
        if current_points < 0:
            raise ValueError("Имеющиеся баллы не могут быть отрицательным числом")
        self.current_points = current_points

        if not isinstance(sum_, int):
            raise TypeError("Сумма покупки должна быть типа int")
        if sum_ < 0:
            raise ValueError("Сумма покупки не может быть отрицательным числом")
        self.sum_ = sum_

    def points_for_purchases(self) -> float:
        """
        Функция, которая показывает количество баллов за покупку
        :return: Баллы за покупку
        Пример:
        >>> buy_in_bookshop = BuyInBookshop(3, 25, 3200)
        >>> buy_in_bookshop.points_for_purchases()
        160
        """
        return self.sum_ // 20

    def coupon(self) -> int:
        """
        Функция, которая возвращает сумму покупки с учетом купона.
        Действует два купона: "Дарим500" при сумме покупки <= 1000, "Дарим1000" при сумме покупки > 1000
        :return: Новая сумма
        Пример:
        >>> buy_in_bookshop = BuyInBookshop(3, 25, 3200)
        >>> buy_in_bookshop.coupon()
        2200
        """
        if self.sum_ <= 1000:
            return self.sum_ - 500
        if self.sum_ > 1000:
            return self.sum_ - 1000


buy_in_bookshop = BuyInBookshop(3, 25, 3200)


if __name__ == "__main__":
    doctest.testmod()  # работоспособность экземпляров класса
