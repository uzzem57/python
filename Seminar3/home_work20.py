my_list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
my_list2 = ['D', 'G']
my_list3 = ['B', 'C', 'M', 'P']
my_list4 = ['F', 'H', 'V', 'W', 'Y' ]
my_list5 = ['K']
my_list6 = ['J', 'X']
my_list7 = ['Q', 'Z']
my_list8 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
my_list9 = ['Д', 'К', 'Л', 'М', 'П', 'У']
my_list10 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
my_list11 = ['Й', 'Ы']
my_list12 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
my_list13 = ['Ш', 'Э', 'Ю']
my_list14 = ['Ф', 'Щ', 'Ъ']
print("Введите слово: ")
n = input().upper()
my_count = 0
for i in range(len(n)):
    if my_list1.count(n[i]) > 0:
        my_count += 1
    elif my_list2.count(n[i]) > 0:
        my_count += 2
    elif my_list3.count(n[i]) > 0:
        my_count += 3
    elif my_list4.count(n[i]) > 0:
        my_count += 4
    elif my_list5.count(n[i]) > 0:
        my_count += 5
    elif my_list6.count(n[i]) > 0:
        my_count += 8
    elif my_list7.count(n[i]) > 0:
        my_count += 10
    elif my_list8.count(n[i]) > 0:
        my_count += 1
    elif my_list9.count(n[i]) > 0:
        my_count += 2
    elif my_list10.count(n[i]) > 0:
        my_count += 3
    elif my_list11.count(n[i]) > 0:
        my_count += 4
    elif my_list12.count(n[i]) > 0:
        my_count += 5
    elif my_list13.count(n[i]) > 0:
        my_count += 8
    elif my_list14.count(n[i]) > 0:
        my_count += 10
print(my_count)