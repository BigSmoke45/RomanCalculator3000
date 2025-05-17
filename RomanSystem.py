from Exception import Over3000
from Exception import ZeroOrLess
from ArabSystem import ArabSystem

class RomanSystem:
    """Клас для конвертації з римської системи в арабську та виконання операцій калькулятора.
    """
    def __init__(self, data_line, part):
        """Конструктор, що приймає значення data_line та part.
        data_line — число у римській системі (рядок)
        self.part — перше числове значення, rhs.part — друге числове значення (обидва в арабській системі)
        """
        self.data_line = data_line
        self.part = part

    def romanToInt(self):
        """Метод для конвертації числа з римської системи в арабську.
        """
        d = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
        n = [d[i] for i in self.data_line.lower() if i in d]
        return sum([i if i >= n[min(j+1, len(n)-1)] else -i for j, i in enumerate(n)])

    def __gt__(self, rhs):
        """__gt__ — перевантаження арифметичного оператора Більше;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part > rhs.part)

    def __ge__(self, rhs):
        """__ge__ — перевантаження арифметичного оператора Більше або дорівнює;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part >= rhs.part)

    def __lt__(self, rhs):
        """__lt__ — перевантаження арифметичного оператора Менше;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part < rhs.part)

    def __le__(self, rhs):
        """__le__ — перевантаження арифметичного оператора Менше або дорівнює;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part <= rhs.part)

    def __eq__(self, rhs):
        """__eq__ — перевантаження арифметичного оператора Дорівнює;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part == rhs.part)

    def __ne__(self, rhs):
        """__ne__ — перевантаження арифметичного оператора Не дорівнює;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        return (self.part != rhs.part)

    def __add__(self, rhs):
        """__add__ — перевантаження арифметичного оператора Додавання;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        plus = int(self.part + rhs.part)
        plus_in_roman = ArabSystem(plus).intToRoman()
        rezult = str(plus_in_roman)
        return rezult

    def __sub__(self, rhs):
        """__sub__ — перевантаження арифметичного оператора Віднімання;
        """
        if self.part > 3000 or rhs.part > 3000:
            raise Over3000
        if self.part <= rhs.part:
            raise ZeroOrLess
        minus = int(self.part - rhs.part)
        minus_in_roman = ArabSystem(minus).intToRoman()
        rezult = str(minus_in_roman)
        return rezult
