num = int(input())
date_dict = {}
for i in range(num):
    name, month, date = input().split()
    month = int(month)
    date = int(date)
    if (month, date) in date_dict:
        date_dict[(month, date)].append(name)
    else:
        date_dict[(month, date)] = [name]
print(date_dict)
# {(3, 2): ['Avril', 'Tim', 'Bill'], (4, 5): ['Candy', 'Sufia', 'Lagrange']}

birthday_same = []
for date, name_list in date_dict.items():
    if len(name_list) > 1:
        birthday_same.append((date, name_list))
print(birthday_same)
# [((3, 2), ['Avril', 'Tim', 'Bill']), ((4, 5), ['Candy', 'Sufia', 'Lagrange'])]

# 对所有的输出，要求按日期从前到后的顺序输出。 对生日相同的名字，按名字从短到长按序输出，长度相同的按字典序输出。
if birthday_same:
    birthday_same.sort()
    print(birthday_same)
# [((3, 2), ['Avril', 'Tim', 'Bill']), ((4, 5), ['Candy', 'Sufia', 'Lagrange'])]

    for birthday, name_list in birthday_same:
        name_list.sort()
        name_list.sort(key=lambda name: len(name))
        line = str(birthday[0]) + " " + str(birthday[1])
        for name in name_list:
            line += " " + name
        print(line)
else:
    print("None")

'''
6
Avril 3 2
Candy 4 5
Tim 3 2
Sufia 4 5
Lagrange 4 5
Bill 3 2
'''