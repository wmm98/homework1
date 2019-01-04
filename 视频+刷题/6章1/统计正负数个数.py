'''
【问题描述】从键盘输入非0整数，以输入0为输入结束标志，求平均值，统计正数负数个数
【输入形式】

      每个整数一行。最后一行是0，表示输入结束。

【输出形式】

     输出三行。

     第一行是平均值。第二行是正数个数。第三行是负数个数。

【样例输入】

                        1

                        1

                        1

                        0


【样例输出】

                        1

                        3

                        0

'''

num_list = []
while True:
    n = int(input())
    num_list.append(n)
    if n == 0:
        break

result = 0
flag = 0
count = 0
for i in num_list:
    result += i
    if i > 0:
        flag += 1
    if i < 0:
        count += 1
# print(len(num_list))
# print(num_list)
# print(result)
avg = result / (len(num_list) - 1)
print(avg)
print(flag)
print(count)
