'''
给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。

【输入形式】

第一行包含一个整数n，表示给定数字的个数; 第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。

【输出形式】

输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。
如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。

【样例输入】

12

5 2 3 3 1 3 4 2 5 2 3 5

【样例输出】

3 4

2 3

5 3

1 1

4 1


【样例说明】

n不超过1000，给出的数为2,000,000,000以内的非负整数。'''
n = int(input())

dic = {}
if n <= 1000:
    num = [int(i) for i in input().split()]
    for r in num:

        if 0 <= r <= 2000000000:
            d = {r: num.count(r)}
            dic.update(d)

# 根据值排序
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(result)
result1 = []
# 将元组转为列表
for i in result:
    i = list(i)
    result1.append(i)
# print(result1)

for a in range(len(result1)):
    for b in range(a + 1, len(result1)):
        if result1[a][1] == result[b][1] and result1[a][0] > result1[b][0]:
            result1[a], result1[b] = result1[b], result1[a]
            # print(result1)


# print(result1)

for i in result1:
    print(i[0], i[1])

# 赖红
# numCount = int(input())
# nums = input().split()
# result = {}
# for i in nums:
#     if i not in result:
#         result[int(i)] = nums.count(i)
#
# # 根据字典的键去排序
# r = {}
# for k in sorted(result.keys()):
#     d = {k: result[k]}
#     r.update(d)
# print(r)
# {1: 1, 2: 3, 3: 4, 4: 1, 5: 3}
# # 转换成列表，键值对变成元组
# temp = r.items()
# print(temp)
# # dict_items([(1, 1), (2, 3), (3, 4), (4, 1), (5, 3)])
# # 想按照值排序字典，可以转换为列表键值对变成元组
# def getKey(x):
#     return x[1]
#
#
# # 根据元组的第二个值排序，倒序
# finallyResult = sorted(temp, key=getKey, reverse=True)
# print(finallyResult)
# # [(3, 4), (2, 3), (5, 3), (1, 1), (4, 1)
# # 输出列表里面的元组的各值
# for i in finallyResult:
#     print(i[0], i[1])







