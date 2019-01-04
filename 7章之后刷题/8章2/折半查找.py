'''【问题描述】

    编写程序实现对单调递增的整型数组进行折半查找。
            
    用折半查找法找出一个数是数组中第几个元素，如果找到，则返回其下标；如果该数不在数组中，则返回-1。
【输入形式】

    输入的第一行为一个非负整数len，表示数组长度；
    输入的第二行为一组整数，表示数组元素，以空格分隔
    输入的第三行为一个整数key，表示要查找的值
【输出形式】

    输出的一行为：若找到，则输出下标；若未找到，则输出“not found”;；若输入的数组不是单调递增，则输出“illegal input”。

【样例输入】

10
1 2 3 4 5 6 7 8 9 10
5
【样例输出】

           4
【样例说明】

        4是数字5在数组中的下标（从0开始编号）。'''

length = int(input())
num = [int(i) for i in input().split()]
key = int(input())
flag = 0
for i in range(length - 1):
    if num[i + 1] <= num[i]:
        print("illegal input")
        flag += 1
        break
if flag == 0:
    if key not in num:
        print("not found")
    else:
        print(num.index(key))




