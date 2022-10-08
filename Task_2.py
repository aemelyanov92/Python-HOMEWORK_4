# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#
# in
# 54
#
# out
# [2, 3, 3, 3]

# Обычный вариант
# n = int(input())
# i = 2
# while n > 1:
#     while n % i == 0:
#         print(i, end=' ')
#         n //= i
#     i += 1
# Второй вариант
# num = int(input())
# list_simple = []
# simple = 2
# while num > 1:
#     if num % simple == 0:
#         list_simple.append(simple)
#         num = num/simple
#     else:
#         simple += 1
# print(list_simple)

# Третий вариант - нравится больше всего
# def factors(num, d=2):
#     while num > 1:
#         n1, n2 = divmod(num, d)
#         if n2:
#             d += 1
#         else:
#             yield d
#             num = n1
#
# n = int(input("Введите, пожалуйста, число: "))
# print('{} = {}' .format(n, ' * '.join(map(str, factors(n)))))

# Четвёртый вариант:
def find_prim_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num /= di
        else:
            di +=1
    return pr_fact


print(find_prim_nums(int(input())))
