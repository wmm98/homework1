'''编写猜数游戏程序，功能是：允许用户反复输入数，直至猜中程序选定的数（假定为100）
。输入的数如果大于选定的数，则提示"larger than expected"；如果小于选定的数，则提示"less than expected"
；如果等于选定的数，则输出"you win"并结束程序。 
【输入形式】

一次或多次输入整数
【输出形式】

对于每一次输入，新起一行输出对于的提示。

【样例输入】

50

150

100

【样例输出】

less than expected

larger than expected

you win

【说明】

被猜的数设定为100。
'''

i = 100
result = []
while True:
    n = int(input())
    result.append(n)
    if n == 100:
        break
for j in result:
    if j < 100:
        print("less than expected")
    elif j > 100:
        print("larger than expected")
    else:
        print("you win")
