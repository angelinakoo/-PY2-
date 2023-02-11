import doctest


class Guitar:
    """ Базовый класс. """
    def __init__(self, name_guitar: str, price_guitar: int, discount_guitar: int):
        """
        Создание и подготовка к работе объекта "Гитара"
        :param name_guitar: Название гитары
        :param price_guitar: Стоимость гитары
        :param discount_guitar: Скидка в %
        Пример:
        >>> guitar = Guitar("YAMAHA PAC612VIIFM", 100000, 10)  # инициализация экземпляра класса
        """
        self._name_guitar = name_guitar
        self._price_guitar = price_guitar
        self._discount_guitar = discount_guitar

    @property
    def name_guitar(self) -> str:
        return self._name_guitar

    @property
    def price_guitar(self) -> int:
        return self._price_guitar

    @price_guitar.setter
    def price_guitar(self, price_value: int) -> None:
        if not isinstance(price_value, int):
            raise TypeError("Стоимость гитары должна быть типа int")
        if price_value <= 0:
            raise ValueError("Стоимость гитары должна быть положительным числом")
        self._price_guitar = price_value

    @property
    def discount_guitar(self) -> int:
        return self._discount_guitar

    @discount_guitar.setter
    def discount_guitar(self, discount_value: int) -> None:
        if not isinstance(discount_value, int):
            raise TypeError("Скидка должна быть типа int")
        if discount_value < 0:
            raise ValueError("Скидка не может быть отрицательным числом")
        if discount_value >= 100:
            raise ValueError("Скидка не может быть больше или равна 100%")
        self._discount_guitar = discount_value

    def __str__(self):
        return f"Компания Yamaha представляет гитару {self._name_guitar}. Цена данной модели - {self._price_guitar}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name_guitar!r}, price={self._price_guitar}, discount={self._discount_guitar}%)"

    def is_here_discount(self) -> str:
        """
        Функция, которая проверяет есть ли скидка на товар
        :return: Имеется ли скидка
        Пример:
        >>> guitar = Guitar("YAMAHA PAC612VIIFM", 100000, 10)
        >>> guitar.is_here_discount()
        'Скидка имеется на данный продукт!'
        """
        if self._discount_guitar == 0:
            return 'Скидки нет!'
        if self._discount_guitar > 0:
            return 'Скидка имеется на данный продукт!'

    def final_price(self) -> float:
        """
        Функция, которая возвращает сумму покупуи, учитывая скидку.
        :return: конечная стоимость
        Пример:
        >>> guitar = Guitar("YAMAHA PAC612VIIFM", 100000, 10)
        >>> guitar.final_price()
        90000.0
        """
        return self.price_guitar - self.price_guitar * self.discount_guitar / 100


class ElectricGuitar(Guitar):
    def __init__(self, name_guitar: str, price_guitar: int, discount_guitar: int, price_combo: int):
        super().__init__(name_guitar, price_guitar, discount_guitar)
        """
        Создание и подготовка к работе дочернего класса "Электрогитара".
        Добавлен новый параметр
        :param price_combo: Цена комбоусилителя
        Остальные параметры наследуются из базового класса.
        Пример:
        >>> electricguitar = ElectricGuitar("YAMAHA PAC612VIIFM", 100000, 10, 30000)
        """
        self._price_combo = price_combo

    @property
    def price_combo(self) -> int:
        return self._price_combo

    @price_combo.setter
    def price_combo(self, price_combo_value: int) -> None:
        if not isinstance(price_combo_value, int):
            raise TypeError("Стоимость комбоусилителя должна быть типа int")
        if price_combo_value < 0:
            raise ValueError("Стоимость комбоусилителя должна быть положительным числом или равна нулю, если комбоуселитель не нужен")
        self._price_combo = price_combo_value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name_guitar!r}, price={self._price_guitar}, discount={self._discount_guitar}%, price_combo={self._price_combo})"

    def final_price(self) -> float:
        """
        Перезагружаем функцию, которая теперь возвращает сумму покупки,
        учитывая скидку и стоимость комбоуселителя, если его решили приобрести.
        :return: конечная стоимость
        Пример:
        >>> electricguitar = ElectricGuitar("YAMAHA PAC612VIIFM", 100000, 10, 30000)
        >>> electricguitar.final_price()
        120000.0
        """
        return self._price_combo + self.price_guitar - self.price_guitar * self.discount_guitar / 100


guitar = Guitar("YAMAHA PAC612VIIFM", 100000, 10)
electricguitar = ElectricGuitar("YAMAHA PAC612VIIFM", 100000, 10, 30000)

if __name__ == "__main__":
    doctest.testmod()
