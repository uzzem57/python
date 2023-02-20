# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста.
# У нас труб будет больше.
#
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна
# только одной данной работающей трубой (в часах). Затем после пустой строки перечислены трубы,
# которые будут заполнять бассейн. Сколько минут на это потребуется?
#
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
#
# Результат запишите в файл time.txt
#
# Пример
# Ввод
#
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273

data1 = open('pipes.txt', 'r', encoding='utf - 8')
data2 = open("text.txt", "w", encoding='utf - 8')
my_line = [line.rstrip() for line in data1]
my_list = []
my_list_ret = []
flag = 0

for line in my_line:
    if flag == 0:
        if line != '':
            my_list.append(int(line))
        else:
            flag += 1
    else:
        c = line.split()
        for i in c:
            my_list_ret.append(my_list[int(i) - 1])

data2.write(str(60 / sum([1 / i for i in my_list_ret])))

data2.close()
data1.close()