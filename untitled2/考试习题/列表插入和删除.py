'''
【问题描述】
输入n(n>1)个正整数，每次将输入的整数插入到列表头部。-1表示输入结束。再输入一个正整数，
在列表中查找该数并删除它。要求输出进行删除操作后的列表。 
【输入形式】
输入以空格分隔的n个整数，以-1结束输入，再输入一个要删除的整数。

【输出形式】
从列表第一个元素开始，输出所有元素。以空格分隔。

【样例输入】
2 4 6 7 8 4 -1
2 
【样例输出】
4 8 7 6 4
【样例说明】
输入以空格分隔的n个整数2 4 6 7 8 4, 以-1结束输入
然后输入2，删除2之后输出剩余整数。
'''

num = input().split()
n = int(input())
num_list = []
for i in num:
    i = int(i)
    num_list.append(i)
# print(num_list)
new_list = num_list[:-1]
# new_list = num_list[::-1]
# print(num_list)
# print(new_list)
newest_list = new_list[::-1]
while n in newest_list:
    for j in newest_list:
        if j == n:
            newest_list.remove(j)
            break
for r in newest_list:
    print(r, end=" ")




