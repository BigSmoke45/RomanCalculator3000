class MyError(Exception):
    """Клас реалізує вихід із певного циклу в програмі та завершує її роботу.
    """
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return f"\nУвага! {self.txt}"

class Over3000(MyError):
    """Клас, який повідомляє користувача, що введене числове значення не може бути більше 3000.
    """
    def __init__(self, text="За умовою завдання максимальне введене число не може бути більше за 3000!"):
        self.txt = text

    def __str__(self):
        return f"\nПомилка! {self.txt}"

class ZeroOrLess(MyError):
    """Клас, який повідомляє про помилку при виконанні операції віднімання, якщо результат менший або дорівнює нулю.
    """
    def __init__(self, text="Результат не може бути меншим або дорівнювати 0!"):
        self.txt = text

    def __str__(self):
        return f"\nПомилка! {self.txt}"

class ErrorNumber(MyError):
    """Клас, який повідомляє про помилку некоректного введення значення.
    """
    def __init__(self, text="Ви ввели некоректне значення!"):
        self.txt = text

    def __str__(self):
        return f"\nПомилка! {self.txt}"
