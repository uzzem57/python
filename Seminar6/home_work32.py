# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

my_list = [random.randint(0,100) for _ in range(int(input("Введите количество элементов массива: ")))]
a = int(input("Введите начало заданного диапазона: "))
b = int(input("Введите конец заданного диапазона: "))
print(my_list)
my_list_index = []
for i in range(len(my_list)):
    if a < my_list[i] < b:
        my_list_index.append(i)
print(my_list_index)