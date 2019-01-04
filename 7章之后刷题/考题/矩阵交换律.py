'''对于矩阵来说，矩阵乘法具有结合律和分配率，但不具有交换率。（二维数组）然而，对于n*n的两个方阵A, B来说，
可能两者的乘法具有A*B = B*A（其中*为矩阵乘法），我们称这两个方阵关于矩阵乘法具有交换性质。请你编写函数comm，
判定给定的两个4阶方阵（即4X4矩阵）是否具有交换性质。

然后编写程序，输入两个4阶矩阵，判定是否具有交换性质，若是则输出yes，否则输出no。

 

【输入格式】

一开始有4行，每行有4个整数，用空格分隔，表示矩阵A；

接下来还有4行，每行有4个整数，用空格分隔，表示矩阵B；

 

【输出格式】

输出只有一行，若输入的两个矩阵具有交换律，输出yes，否则输出no。

 

样例输入

2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2
2 2 2 2

 

样例输出

yes'''


def comm(ju1, ju2):
    result = []
    for r in range(5):
        row = []
        for c in range(5):
            v = ju1[r][0] * ju2[0][c] + ju1[r][1] * ju2[1][c] + ju1[r][2] * ju2[2][c] + ju1[r][3] * ju2[3][c]
            row.append(v)
        result.append(row)

    result1 = []
    for r1 in range(4):
        row1 = []
        for c1 in range(4):
            v1 = ju2[r1][0] * ju1[0][c1] + ju2[r1][1] * ju1[1][c1] + ju2[r1][2] * ju1[2][c1] + ju2[r1][3] * ju1[3][c1]
            row1.append(v1)
        result1.append(row1)
    if result == result1:
        print("yes")
    else:
        print("no")

ju1 = []
for i in range(4):
    num1 = [int(i) for i in input().split()]
    ju1.append(num1)
ju2 = []
for j in range(4):
    num2 = [int(j) for j in input().split()]
f = comm(ju1, ju2)