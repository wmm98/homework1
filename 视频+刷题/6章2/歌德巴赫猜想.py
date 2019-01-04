'''
证明在偶数n以内，歌德巴赫猜想是成立的。歌德巴赫猜想是：任何一个充分大的偶数都可以表示为两个素数之和。
例如,4=2+2   6=3+3   8=3+5  50=3+47。


【输入形式】

输入偶数n
【输出形式】

对每一个偶数4, 6, 8, ..., n，依次输出一行。该行内容是<偶数>=<素数1>+<素数2>，要求素数1<=素数2.
【样例输入】

6
【样例输出】

4=2+2

6=3+3
'''


def su_shu(m):
    # 素数大于1
    if m > 1:
        for r in range(2, m):
            if m % r == 0:
                return False
        else:
            return True
    # 小于等于1的不是素数
    else:
        return False


n = int(input())
num = 4
while num <= n:

    # 素数1 >= 素数2，可以控制第二个素数
    for i in range(2, n):
        flag = 0
        for j in range(i, n):
            if su_shu(i) and su_shu(j) and i + j == num:
                print("%d=%d+%d" % (num, i, j))
                flag += 1
        if flag == 1:
            break
    num += 2
