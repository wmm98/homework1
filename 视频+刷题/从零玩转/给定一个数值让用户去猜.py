
# 给定一个数值
num = 90
flag = 0
while True:
    flag += 1
    # 用户输入一个数值
    num1 = int(input())

    # 如果数值数值相等，就输出“你猜对了”，并且退除程序
    if num1 == num:
        print("你猜对了，一共猜了%d次" % flag)
        exit()  # 在这里用break来结束循环也可以

    # 如果数值大于给定数值，则输出“大了”，反之，输出小了
    if num1 > num:   # 这里不用接着上面用else也可以，上面的if语句执行了，会直接退出循环，并不会影响到下面的代码
        print("大了点")
    else:
        print("小了点")


# 用户继续猜
# 最后也要打印用户猜了多少次