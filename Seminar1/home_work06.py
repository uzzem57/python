# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

a = input()
summa1 = 0
summa2 = 0
if len(a) != 6:
    print("Вы ввели не верное количество цифр")
else:
    for i in range(0,3):
        summa1 = summa1 + int(a[i])
    for i in range(3,6):
        summa2 = summa2 + int(a[i])
if summa1 == summa2:
    print("yes")
else:
    print("no")