number = 98
guess = input("我记住了一个1~100之间的整数。你猜是什么数：")
guess = int(guess)

if guess == number:
    print("你猜中了！厉害！")
elif guess > number:
    print("你猜大了。")
else:
    print("你猜小了")


# C:\Users\吴铭明\PycharmProjects\untitled2\大作业\guess_once.py