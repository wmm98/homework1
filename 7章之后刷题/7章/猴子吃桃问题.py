'''
【问题描述】猴子吃桃问题：
                猴子摘下若干个桃子，第一天吃了桃子的一半多一个，以后每天吃了前一天剩下的一半多一个，
                到第n天吃以前发现只剩下一个桃子，
            编写程序实现：据输入的天数计算并输出猴子共摘了几个桃子

【输入形式】输入的一行为一个非负整数，表示一共吃的天数。
【输出形式】输出的一行为一个非负整数，表示共摘了几个桃子，若输入的数据不合法（如：负数或小数），则输出"illegal data"。
【样例输入】3
【样例输出】10

【样例输入2】0
【样例输出2】0
'''
try:
    days = int(input())
    n = 1
    if days == 0:
        print(0)
    elif days < 0:
        print("illegal data")
    else:
        # 从最后一天推到第一天
        while days > 1:
            n = (n + 1) * 2
            days -= 1
        print(n)
except(ValueError):
    print("illegal data")