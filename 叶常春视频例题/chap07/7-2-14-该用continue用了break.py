#例7-2-14  分奇数偶数
#本例在例7-2-9基础上进行改动。
#功能：输入一组整数，去掉负数，然后分成奇数和偶数。
#1. 输入一组数
ss = input("输入一组整数，用空格隔开：").split()

#2. 分奇数偶数
evens = []
odds = []
for s in ss:
    n = int(s)
    if n < 0:
        break  #去掉负数。
        #上一行用了break,有什么后果？

    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

#3. 输出
print("奇数有：", odds)
print("偶数有：", evens)