# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее
# максимальную длину
# (или список слов, если таковых несколько).

def longest_words(file):
    my_list = []
    with open(file, 'r', encoding='utf - 8') as file:
        for i in file.read().splitlines():
            my_list.append(i)
        my_list_rez =[]
        for i in my_list:
            my_list_rez.append(i.split())
            my_list_ret = [i for group in my_list_rez for i in group]
        str_max = len(max(my_list_ret, key=len))
        for i in my_list_ret:
            if len(i) == str_max:
                print(i)
longest_words("article.txt")
