'''
【问题描述】
在屏幕上显示如下杨辉三角形：
                             1
                         1      1
                     1      2      1
                 1       3     3       1
             1       4      6      4       1
         1       5      10     10      5       1
      

【输入形式】
从键盘输入整数n（n>=0且n<=12）
【输出形式】
在屏幕上输出n+1行杨辉三角形。

【输入样例】 
3
【输出样例】
------***1

----***1***1

--***1***2***1

***1***3***3***1

其中－和*都是空格位

即每个数字占四位！

【输出样例说明】

每个数字占四位。这意味着，数字12的输出形式是**12， 这里**代表两个空格。数字330的输出形式是*330。这里*代表一个空格。

要输出占4格的数字num，使用以下语句：

      print("%4d" % num)

%4d是指输出一个整数，其中的4表示占4格。
【评分标准】
结果完全正确得20，每个测试点4分。'''

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