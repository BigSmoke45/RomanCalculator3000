from RomanSystem import RomanSystem
from ArabSystem import ArabSystem
from Exception import Over3000
from Exception import ZeroOrLess
from Exception import ErrorNumber
from Exception import MyError

if __name__ == "__main__":
    operations = {
        1: '>',
        2: '>=',
        3: '<',
        4: '<=',
        5: '==',
        6: '!=',
        7: '+',
        8: '-'
    }

import json
nums = ["1 = I", "4 = IV", "5 = V", "9 = IX", "10 = X", "40 = XL", "50 = L", "90 = XC", "100 = C", "400 = CD", "500 = D", "900 = CM", "1000 = M"]
filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

stop = 0
while stop == 0:
    try:
        print("Деякі числові значення у римській системі:")
        file = 'nums.json'
        with open(file) as fl:
            nums_new = json.load(fl)
        print(nums_new)
        a_rom = input("Введіть перше число у римській системі (від 1 до 3000): ")
        if a_rom.upper() == "СТОП":
            stop += 1
            raise MyError("Завершення роботи програми")
        a_int = RomanSystem(a_rom, 0).romanToInt()
        if a_int == 0:
            raise ErrorNumber
        b_rom = input("Введіть друге число у римській системі (від 1 до 3000): ")
        if b_rom.upper() == "СТОП":
            stop += 1
            raise MyError("Завершення роботи програми")
        b_int = RomanSystem(b_rom, 0).romanToInt()
        if b_int == 0:
            raise ErrorNumber
    except MyError as me:
        print(me)
    except ErrorNumber as en:
        print(en)
    else:          
        for key, value in operations.items():
            print("{0}: {1}".format(key, value))
        operation_number = int(input("\nВведіть номер операції: "))
        aComp = RomanSystem(0, a_int)
        bComp = RomanSystem(0, b_int)
        if operation_number == 1:
            print(f"Операція {a_rom} > {b_rom}: {aComp > bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp > bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 2:
            print(f"Операція {a_rom} >= {b_rom}: {aComp >= bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp >= bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 3:
            print(f"Операція {a_rom} < {b_rom}: {aComp < bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp < bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 4:
            print(f"Операція {a_rom} <= {b_rom}: {aComp <= bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp <= bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 5:
            print(f"Операція {a_rom} == {b_rom}: {aComp == bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp == bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 6:
            print(f"Операція {a_rom} != {b_rom}: {aComp != bComp}")
            print("Конвертація в арабську систему: ", a_int, f" {operations[operation_number]} ", b_int, f": {aComp != bComp}")
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 7:
            c_rom = aComp + bComp
            c_int = RomanSystem(c_rom, 0).romanToInt()
            print("Результат у римській системі: ", a_rom, f" {operations[operation_number]} ", b_rom, " = ", c_rom)
            print("Результат в арабській системі: ", a_int, f" {operations[operation_number]} ", b_int, " = ", c_int)
            input("Натисніть будь-яку клавішу для продовження")
        elif operation_number == 8:
            print(f"Операція {a_rom} - {b_rom}: ")
            c_rom = aComp - bComp
            c_int = RomanSystem(c_rom, 0).romanToInt()
            print("Результат у римській системі: ", a_rom, f" {operations[operation_number]} ", b_rom, " = ", c_rom)
            print("Результат в арабській системі: ", a_int, f" {operations[operation_number]} ", b_int, " = ", c_int)
            input("Натисніть будь-яку клавішу для продовження")
        else:
            input("Ви ввели неправильне значення! Натисніть будь-яку клавішу для продовження")
