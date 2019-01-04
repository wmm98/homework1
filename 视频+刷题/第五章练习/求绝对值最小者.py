'''	
【问题描述】编写程序实现：计算并输出标准输入的三个数中绝对值最小的数。
            
【输入形式】标准输入的每一行表示参与计算的一个数。
【输出形式】标准输出的一行表示输入的三个数中绝对值最小的数,如果有多个,以一个空格作为间隔.
【样例输入】
－1
3
1 
【样例输出】
-1.0 1.0
【样例说明】
【评分标准】

'''

n = float(input())
n1 = float(input())
n2 = float(input())
n_list = []
n_list.append(n)
n_list.append(n1)
n_list.append(n2)

# print("%0.1f" % min(abs(n), abs(n1), abs(n2)))
for i in n_list:
    if min(abs(n), abs(n1), abs(n2)) == abs(i):
        print("%0.1f" % i, end=" ")