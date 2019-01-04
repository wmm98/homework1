'''【问题描述】

从标准输入中读入两个整数集，整数集中数据无序，且可能有重复数据。当两个数据集中数据完全相同（数据相同，数据若重复，重复个数也相同，顺序不一定相同），则两个数据集相同。编写一程序判断输入的两数据集是否相同：用1表示相同，用0表示不同。

【输入形式】

先输入第一组整数集的个数（大于等于1，小于等于20），然后输入第一组整数（以一个空格分隔）；再输入第二组整数集的个数（大于等于1，小于等于20），并输入第二组整数（以一个空格分隔）。

【输出形式】

若两数据集相同，则输出1，否则输出0，然后按照从小到大的顺序分行输出第一个数据集中的数据及重复个数（以一个空格分隔数据和重复个数）。

【样例输入1】

10
100  56  7  89  -12  100  7  -12  100  56
10
-12  7  7  56  100  -12  100  56  89  100

【样例输出1】

1
-12   2
7   2
56   2
89   1
100   3

【样例输入2】

10
56  70  -12  100  7  89  -12  100  56  1001
9
1001  56  70  89  -12  100  7  -12  100

【样例输出2】

0
-12   2
7   1
56   2
70   1
89   1
100   2
1001   1

【样例说明】

样例1中输入的两个数据集的数据和各个数据的重复个数都完全相同，所以输出1，然后按从小到大的顺序输出第一个
数据集中的数据及重复个数（即：有2个-12，2个7，2个56，1个89，3个100）。
样例2中输入的两个数据集中的数据相同，但第一个数据集中有2个56，而第二个数据集中有1个56，所以两个数据集不同，
输出0，并按从小到大的顺序输出第一个数据集中的数据及重复个数。'''

n = int(input())
num1 = [int(i) for i in input().split()]
n1 = int(input())
num2 = [int(i) for i in input().split()]

num11 = sorted(num1)
num22 = sorted(num2)
if num11 == num22:
    print("1")
else:
    print("0")
result = []

for i in num11:
    if i in num22:
        if num11.count(i) <= num22.count(i):
            if [i, num22.count(i)] not in result:
                result.append([i, num22.count(i)])
        else:
            if [i, num11.count(i)] not in result:
                result.append([i, num11.count(i)])

# print(result)
for j in result:
    print(j[0], j[1])




