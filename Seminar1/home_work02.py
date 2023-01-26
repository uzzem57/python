# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input())
summa = 0
while a > 0:
    summa += a%10
    a = a//10
print(summa)

# Второй вариант
# a = input()
# summa = 0
# for i in range(0, len(a)):
#    summa = summa + int(a[i])
# print(summa)