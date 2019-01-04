'''
【问题描述】
输入三位数字N，求两位数AB（其中个位数字为B，十位数字为A，且有0 < A < B <=9）。使得下列等式成立：
 AB x BA = N
其中BA是把AB中个、十位数字交换所得的两位数。
 
编写程序，接收控制台输入的三位整数N，求解A，B并输出。
如果没有解则输出No Answer。
 
【输入形式】
 
从键盘输入整数N。
 
【输出形式】

输出只有一行，包含两个数字A和B。输出时两个数字紧密输出，不使用其它字符进行分隔。
 
【样例输入】

976
 
【样例输出】

16
 
【样例说明】

输入整数N=976。经计算得16*61=976。可得a=1, b=6。将两个字符依次输出。
'''
#
# # 输入N
N = int(input())
#
#while True:
flag = 0
for a in range(1, 10):
    num = range(a + 1, 10)
    for b in num:
        if (a * 10 + b) * (b * 10 + a) == N:
            print(a * 10 + b)
            flag += 1
            break
if flag != 1:
    print("No Answer")
    # break
# else:
#     print("No Answer")
#     break

# for i in range(10):
#     # if i == 9:
#     #     print('found it! i = %s' % i)
#     break
# else:
#     print('not found it ...')
# # 像这种情况就没有输出
#

# 当for中没有break跳出循环的时候，无论怎么样都会输出else语句的内容
# 当for中有break语句跳出循环时，for执行不成功时，输出else语句，执行成功时不输出else语句

# count = 5
# while count < 4:
#    print("--------")
#    count += 1
#    break
# else:
#    print("输出else语句")
#
# # while 与else连用的情况跟for else的用法一样