# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("Введите первый элемент: "))
n = int(input("Введите количество элементов: "))
d = int(input("Введите разность: "))
my_list = []
for i in range(1,n + 1):
    my_list.append(a1 + (i-1) * d)
print(my_list)