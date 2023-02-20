my_list = [2, 5, 7, 3, 5, 2, 6, 8, 9]
sqr = 1
my_rez =[]
with open('file.txt', 'r', encoding='utf - 8') as file:
    for i in file.read().splitlines():
        my_rez.append(i)
for i in my_rez:
    sqr = sqr * my_list[int(i)]
print(sqr)
