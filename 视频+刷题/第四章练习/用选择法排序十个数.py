'''
用选择法对10个整数进行从小到大的排序。
这里采用的选择法的思路是进行9轮比较和交换：（1）遍历10个数，选出最小的数，该数和10个数中首位置的数进行交换；
（2）遍历末尾的9个数，选出最小的数，该数和末尾9个数中首位置的数的进行交换；
（3）遍历末尾的8个数，选出最小的数，交换至末尾8个数中首位置，......，依次类推，直至排序完成。
【输入形式】
输入十个整数
【输出形式】
输出9行。
前8行是9轮比较和交换后的整数序列。
第9行是排序后的十个整数。
数之间用空格隔开。
【样例输入】
4 5 3 6 7 2 1 8 10 9
【样例输出】
1 5 3 6 7 2 4 8 10 9 
1 2 3 6 7 5 4 8 10 9 
1 2 3 6 7 5 4 8 10 9 
1 2 3 4 7 5 6 8 10 9 
1 2 3 4 5 7 6 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 10 9 
1 2 3 4 5 6 7 8 9 10 
'''

# num = input().split()
# num_list = []
#
# for i in num:
#     i = int(i)
#     num_list.append(i)
#
# num_list1 = num_list.copy()
#
# for j in range(len(num_list) - 1):
#     for r in num_list1:
#         if r == min(num_list1):
#             r_index = num_list.index(r)
#             num_list[r_index] = num_list[j]
#             num_list[j] = r
#             num_list1.remove(min(num_list1))
#             break
#
#     # print(num_list)
#
#     for i in num_list:
#         print(i, end=" ")
#     print("")

# 老师代码
def find_min(n_list, start, end):
    ''' 在n_list列表的[start, end]区间内找到最小值的下标 '''
    min_index = start
    for i in range(start + 1, end + 1):  # 1到9
        if n_list[i] < n_list[min_index]:
            min_index = i
    return min_index


n_list = [int(x) for x in input().split()]
len_n_list = len(n_list)
for i in range(len_n_list - 1):
    min_index = find_min(n_list, i, len_n_list - 1)
    # print(min_index)
    if min_index != i:
        n_list[i], n_list[min_index] = n_list[min_index], n_list[i]
    for n in n_list:
        print(n, end = ' ')
    print('')

















