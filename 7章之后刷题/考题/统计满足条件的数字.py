'''【问题描述】输入一个整数k，求1到k以内(不含该整数)能被3整除且个位数为6的所有整数,并输出
【输入形式】一个整数k
【输出形式】一组整数。在一行中从小到大输出，数之间用空格隔开。
【样例输入】7
【样例输出】6
k = int(input()) 
result_list = search(k) 
for r in result_list: 
    print(r, end=' ')'''
def search(k):
    list1 = []
    for i in range(1, k):
        result = i % 3
        i1 = str(i)[::-1]
        if result == 0 and int(i1[0]) == 6:
            list1.append(i)
    list2 = sorted(list1)
    return list2

k1 = int(input())
result2 = search(k1)
for r in result2:
    print(r, end=' ')