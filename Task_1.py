# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000

# 1 вариант - без функций
# from decimal import Decimal
# p = '9'
# a = Decimal(p)
# a = a.quantize(Decimal("0.000001"))
# print(a)

# 2 вариант для ДЗ

from decimal import Decimal


def accuracy(num, acc):
    number = Decimal(f"(number)")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Введите число: ")), float(input("Введите требуемую точность 0.0001: "))))