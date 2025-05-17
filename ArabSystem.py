class ArabSystem:
    """Клас для виконання операції конвертації числа з арабської системи в римську.
    """
    def __init__(self, num):
        """Конструктор, який приймає значення num. num — число в арабській системі
        """
        self.num = num

    def intToRoman(self):
        """Метод для виконання операції конвертації числа з арабської системи в римську
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while self.num > 0:
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        return roman_num
