import random

number = random.randint(1, 100)
print("我已经想好了1到100之间的一个数。")
flag = 0
for i in range(6):
    flag += 1
    if flag == 1:
        print("你猜一猜看是什么数：")
        guess = int(input())
    else:
        print("你再猜：")
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

# C:\Users\吴铭明\PycharmProjects\untitled2\大作业\guessNumber.py