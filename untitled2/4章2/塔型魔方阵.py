'''
【问题描述】输入一个自然数Ｎ（1<=N<=9），要求输出如下的魔方阵，即边长为2*N-1，
Ｎ在中心出现一次，其余位置上的数字从外向中心逐渐增大。
N=3时：
11111
12221
12321
12221
11111
N=4时：
1111111
1222221
1233321
1234321
1233321
1222221
1111111
【输入形式】从标准输入读取一个整数N。
【输出形式】向标准输出打印结果。输出符合要求的方阵，每个数字占一个字符宽度，在每一行末均输出一个回车符。
【输入样例】3
【输出样例】
11111
12221
12321
12221
11111
【样例说明】输入自然数3，则输出边长为5的方阵，3在方阵的中间出现一次，其余位置上的数字从外向中心逐渐增大。
 	'''

# 不可行
# n = int(input())
#
# # 表示1到n数字的列表 [1, 2, 3, 4]
# list1 = []
# for i in range(1, 1 + n):
#     list1.append(i)
# print(list1)
#
# # list2 表示一个切取前面的的数字
# list2 = list1[:-1]  # [1, 2, 3]
# print(list2)
#
# # 更新list1,整个列表形成回文
# for j in list2[::-1]:
#     list1.append(j)
# print(list1)  # [1, 2, 3, 4, 3, 2, 1]
#
# all_list = [list1]
# r = 0
# for a in list1:
#     if a == n:
#         r = list1.index(a)
#         list1[r] == n - 1
#         n -= 1
#     if n == 0:
#         break
#
# all_list.append(list1)
# print(all_list)


# 赖红
# N = int(input())
# temp = []
# result = []
# # 生成矩阵，里面的值默认全部是0
# for i in range(2*N-1):
#     for j in range(2*N-1):
#         temp.append(0)
#     result.append(temp)
#     temp = []
#
# print(result)
# # 生成一个长度为2*N - 1的矩阵
#
# # 不断变化的值，用于赋值给矩阵里面的
# flag = 1
# # 修改矩阵里面的值
# for i in range(N):
#     for j in range(i, N*2-(i+1)):
#         result[j][i] = result[i][j] = result[j][2*N-(2+i)] = result[2*N-2-i][j] = flag
#     flag += 1
#     print(result)
#
# # 输出最后的矩阵结果
# for i in result:
#     for j in i:
#         print(j, end="")
#     print()

N = int(input())

num_list = [[0 for i in range(2 * N - 1)] for i in range(2 * N - 1)]
print(num_list)

flag = 1
for i in range(N):
    for j in range(i, 2 * N - i - 1):
        num_list[i][j] = num_list[j][i] = num_list[j][2 * N - i - 2] = num_list[2 * N - 2 - i][j] = flag
    flag += 1
for r in num_list:
    for y in r:
        print(y, end=" ")
    print()