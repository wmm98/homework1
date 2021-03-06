'''【问题描述】输入整数N( 1 <= N <= 10 )，生成从1~N所有整数的全排列。 

【输入形式】输入整数N。

【输出形式】输出有N!行，每行都是从1~N所有整数的一个全排列，各整数之间以空格分隔。各行上的全排列不重复。
输出各行遵循"小数优先"原则, 在各全排列中，较小的数尽量靠前输出。如果将每行上的输出看成一个数字，则所有输出构成升序数列。
具体格式见输出样例。

【样例输入1】1

【样例输出1】1 

【样例说明1】输入整数N=1，其全排列只有一种。

【样例输入2】3  

【样例输出2】

1 2 3

1 3 2

2 1 3

2 3 1

3 1 2

3 2 1

【样例说明2】输入整数N=3，要求整数1、2、3的所有全排列, 共有N!=6行。且先输出1开头的所有排列数，
再输出2开头的所有排列数，最后输出3开头的所有排列数。在以1开头的所有全排列中同样遵循此原则。

【样例输入3】10 

【样例输出3】

1 2 3 4 5 6 7 8 9 10

1 2 3 4 5 6 7 8 10 9

1 2 3 4 5 6 7 9 8 10

1 2 3 4 5 6 7 9 10 8

1 2 3 4 5 6 7 10 8 9

1 2 3 4 5 6 7 10 9 8

1 2 3 4 5 6 8 7 9 10

1 2 3 4 5 6 8 7 10 9

1 2 3 4 5 6 8 9 7 10

1 2 3 4 5 6 8 9 10 7'''


import itertools
num = int(input())
n = [m for m in range(1, num+1)]

result = list(itertools.permutations(n))
for i in result:
    for j in i:
        print(j, end=" ")
    print()
