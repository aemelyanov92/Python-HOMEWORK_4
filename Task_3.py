# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
# in
# 7
#
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#

# Черновик
# def awesome_func(lst):
#     res = []
#     for i in lst:
#         res.append(i) if i not in res else None
#     return res
# print()

# def awesome_func(lst):
#     return list(set(lst))


from random import randrange


def list_rand_nums(count: int):
    if count < 0:
        print("Negative number")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


def unic_elem(list_nums: list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)

    return result


all_list = list_rand_nums(int(input("Enter the number: ")))
print(all_list)
print(unic_elem(all_list))

