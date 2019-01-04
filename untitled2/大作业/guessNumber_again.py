import random
import math
continuing = True
while continuing:
    # number = random.randint(1, 100)
    number = random.randint(50, 100001)
    number1 = random.randint(1, number)
    # 计算次数C
    # print(math.log(100, 10))
    c = int(math.log(number, 2))

    print("我已经想好了1到100之间的一个数。")
    for i in range(c):
        print("你猜一猜看是什么数：")
        guess = int(input())

        if guess == number:
            print("你猜对了。恭喜！")
            break
        elif guess < number:
            print("猜小了")
        else:
            print("猜大了")

    if guess != number:
        print("你猜的都不对。我想的数字是" + str(number) + ".")

    print("再猜一轮？(yes/no)")
    continuing = input().lower().startswith('y')



# 1.修改guessNumber_again.py，实现以下功能：把被猜测的数字的范围改为[1, n]，而不是固定的范围[1, 100]。n是随机生成的，且100000>=n>=50。
# 2.当被猜测的数字的范围[1, n]很大时，比如n=10000，让人只猜6次的话，猜不出来的情况是普遍的。于是，我们希望这个猜测次数c可以根据n的大小来决定。
    # 我们约定，两者的关系是：
#     2**c <= n < 2**(c+1)
# 请你继续修改guessNumber_again.py，实现以下功能：据n的大小调整猜测次数c。
# C:\Users\吴铭明\PycharmProjects\untitled2\大作业\guessNumber_again.py