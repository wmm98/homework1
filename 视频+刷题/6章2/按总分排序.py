'''输入n个学生的成绩，按总分从大到小输出。
【输入形式】

第一行输入学生人数n。

后续n行，每一行输入一个学生的学号, 姓名，语文成绩和数学成绩。各字段之间用空格隔开。
【输出形式】

输出n行。每一行给出学生学号，姓名，总分。按总分从大到小排序。若总分相同，则按学号从小到大排序。
【样例输入】

5

355 dj 60 70

665  kk 70 80

g33 He 55 95

l222 Li 60 80

n77 Liu 70 60
【样例输出】

665 kk 150

g33 He 150

l222 Li 140

355 dj 130

n77 Liu 130'''

'''
5
355 dj 60 70
665  kk 70 80
g33 He 55 95
l222 Li 60 80
n77 Liu 70 60
'''
n = int(input())
result = []

for i in range(n):
    s_list = []
    info = input().split()
    # 总得分

    sum = int(info[2]) + int(info[3])
    for j in info[:-2]:
        s_list.append(j)
    s_list.append(sum)
    result.append(s_list)

# print(result)


def get_sort(x):
    return x[0]

l = sorted(result, key=get_sort)


def get_sort1(x):
    return x[2]

l1 = sorted(l, key=get_sort1, reverse=True)


# print(l)

for o in l1:
    for s in o:
        print(s, end=" ")
    print()