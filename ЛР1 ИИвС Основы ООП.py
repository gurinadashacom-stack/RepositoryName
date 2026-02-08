import doctest
from typing import Union


class Book:
    """Абстрактный класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.pages = pages

    def open_page(self, page_number: int) -> bool:
        """
        Открывает книгу на заданной странице.

        :param page_number: Номер страницы для открытия
        :return: True, если страница существует, иначе False

        Примеры:
        >>> book = Book("Python Basics", "Ivanov", 300)
        >>> book.open_page(10)
        True
        >>> book.open_page(500)
        False
        """
        return 1 <= page_number <= self.pages

    def change_author(self, new_author: str) -> None:
        """
        Меняет автора книги.

        :param new_author: Имя нового автора
        :return: None

        Примеры:
        >>> book = Book("Title", "Old Author", 100)
        >>> book.change_author("New Author")
        """
        self.author = new_author


class Phone:
    """Абстрактный класс, описывающий смартфон."""

    def __init__(self, brand: str, model: str, battery_level: int):
        self.brand = brand
        self.model = model

        if not isinstance(battery_level, int) or not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть целым числом от 0 до 100")
        self.battery_level = battery_level

    def make_call(self, number: str) -> bool:
        """
        Совершает звонок по указанному номеру.

        :param number: Номер телефона
        :return: True, если звонок начат, False если телефон разряжен

        Примеры:
        >>> phone = Phone("Apple", "iPhone 15", 50)
        >>> phone.make_call("+79990000000")
        True
        """
        if self.battery_level > 0:
            return True
        return False

    def charge(self, amount: int) -> None:
        """
        Заряжает телефон на указанное количество процентов.

        :param amount: Количество процентов заряда
        :return: None

        Примеры:
        >>> phone = Phone("Samsung", "S23", 10)
        >>> phone.charge(50)
        """
        self.battery_level = min(100, self.battery_level + amount)


class BankAccount:
    """Абстрактный класс, описывающий банковский счет."""

    def __init__(self, account_number: str, balance: Union[int, float]):
        self.account_number = account_number

        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным числом")
        self.balance = balance

    def deposit(self, amount: Union[int, float]) -> float:
        """
        Пополняет счет на указанную сумму.

        :param amount: Сумма пополнения
        :return: Новый баланс счета

        Примеры:
        >>> acc = BankAccount("12345", 1000)
        >>> acc.deposit(500)
        1500.0
        """
        self.balance += amount
        return float(self.balance)

    def withdraw(self, amount: Union[int, float]) -> float:
        """
        Снимает деньги со счета.

        :param amount: Сумма снятия
        :return: Новый баланс счета
        :raises ValueError: Если сумма снятия больше баланса

        Примеры:
        >>> acc = BankAccount("12345", 1000)
        >>> acc.withdraw(200)
        800.0
        """
        # РЕАЛИЗАЦИЯ:
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        return float(self.balance)


if __name__ == "__main__":
    doctest.testmod()