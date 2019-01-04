'''【问题描述】

 输入n个非负整数，统计n个数中各个数字(0~9)出现的次数，并按照由多到少的顺序输出。(n<=1000)

 

【输入格式】

第一行输入正整数n，表示总共有n个数。

接下来的n行为n个非负整数(最大值为2^32-1)。

 

【输出格式】

输出10行，每行有两个数，第一个是数字(0~9)，第二个是该数字出现的次数,中间用一个空格隔开。
按数字出现次数由高到低排序输出,若数字出现的次数相等，则按数字由小到大输出。

 

【样例输入】

5
123
31
1767
0
9786


【样例输出】

1 3

7 3

3 2

6 2

0 1

2 1

8 1

9 1

4 0

5 0 '''

n = int(input())
list2 = []

result = ""
for i in range(n):
    num = int(input())
    for j in str(num):
        result += j

for r in result:
    list1 = [r, result.count(r)]
    if list1 not in list2:
        list2.append(list1)
# print(list2)

no_num = [str(i) for i in range(10)]
for s in no_num:
    if s not in result:
        list3 = [s, 0]
        list2.append(list3)


# 输出10行，每行有两个数，第一个是数字(0~9)，第二个是该数字出现的次数,中间用一个空格隔开。
# 按数字出现次数由高到低排序输出,若数字出现的次数相等，则按数字由小到大输出。
def sort_list(x):
    return x[0]

l = sorted(list2, key=sort_list)

def sort1(a):
    return a[1]

l2 = sorted(l, key=sort1, reverse=True)
for t in l2:
    print(t[0], t[1])


