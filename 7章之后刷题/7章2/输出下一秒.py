'''【问题描述】编写一个程序，输出当前时间的下一秒。
【输入形式】用户在第一行按照小时:分钟:秒的格式输入一个时间。
【输出形式】程序在下一行输出这个时间的下一秒。
【样例输入】23:59:59
【样例输出】0:0:0
【样例说明】用户按照格式输入时间，程序输出此时间的下一秒。'''

n = [int(i) for i in input().split(":")]
# print(n)
if n[2] < 59:
    print(str(n[0]) + ":" + str(n[1]) + ":" + str(n[2] + 1))
else:
    if n[1] < 59:
        print(str(n[0]) + ":" + str(n[1] + 1) + ":" + str(0))
    else:
        if n[0] < 23:
            print(str(n[0] + 1) + ":" + str(0) + ":" + str(0))
        else:
            print(str(0) + ":" + str(0) + ":" + str(0))
