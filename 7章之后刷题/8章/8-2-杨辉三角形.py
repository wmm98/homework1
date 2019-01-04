n = int(input())
num_line = [1]
line_head = ' ' * (2 * n)
print("%s%4d" % (line_head, 1))

num_line = [1, 1]
for i in range(n):
    # 输出
    line_head = ' ' * (2 * (n - i - 1))  # 生成2*(n-i-1)个空格的字符串
    print(line_head, end='')
    for num in num_line:  # num_line: [1, 2, 1]
        print("%4d" % (num), end='')
    print('')  # 换行

    # 下一行的数字序列
    new_num_line = [1]
    for p in range(len(num_line) - 1):  # 第4行： [0, 1, 2]
        new_num_line.append(num_line[p] + num_line[p + 1])
    new_num_line.append(1)
    num_line = new_num_line
