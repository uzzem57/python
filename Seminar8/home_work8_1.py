# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число).


# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).
def read_last(lines, file):
    if lines <= 0:
        print("Введено не положительное целое цисло")
        return
    my_list = []
    with open(file, 'r', encoding='utf - 8') as file:
        for i in file.read().splitlines():
            my_list.append(i)
        if lines > len(my_list):
            print("Столько строк нет в файле")
            return
        for i in range(0, lines):
           print(my_list[len(my_list) - lines + i])
read_last(int(input("Введите количество строк : ")),'article.txt')


