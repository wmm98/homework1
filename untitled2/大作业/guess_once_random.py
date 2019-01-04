import random

number = random.randint(1, 100)
guess = input("我想好了1到100之间的一个整数。你猜是什么数：")
guess = int(guess)

if guess == number:
    print("你猜中了！厉害！")
elif guess > number:
    print("你猜大了")
else:
    print("你猜小了")