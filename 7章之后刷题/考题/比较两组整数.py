'''
【问题描述】
比较两组整数是否有相同的元素，不考虑元素的顺序，并忽略元素重复的情况。例如：
1  4  9  16  9  7  4  9  11
与下列一组整数：
11  7  9  16  4  1
相同。
【输入形式】
分行输入两组整数，以空格分割
【输出形式】
打印两组整数中相同的元素，顺序以第一行的整数输入顺序为准。如果没有相同元素，打印：No Answer。
【输入样例】
1 4 9 16 9 7 4 9 11
11 7 9 16 4 1
【输出样例】

"#"代表空格
1#4#9#16#7#11#
【样例说明】
输入两组整数
1  4  9  16  9  7  4  9  11
11  7  9  16  4  1
由于这两个数组具有相同的元素，顺序打印第一行与第二行相同的元素。
'''

num1 = [int(i) for i in input().split()]
num2 = [int(i) for i in input().split()]

list1 = []
for i in num1:
    if i in num2 and i not in list1:
        list1.append(i)
for j in list1:
    print(j, end=" ")
if len(list1) == 0:
    print("No Answer")