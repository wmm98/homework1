'''【题目描述】

IP地址总是由4个0-255的数字以"."隔开的形式来显示给用户，例如192.168.0.1。在计算机中，
一个IP地址用4字节 来依次存储其从右到左的4个数字部分，每个字节（8比特）以2进制的形式存储相应的IP地址数字，
请你实现一个从IP地址的显示格式到计算机存储格式的转 换。

【输入形式】

每行输入一个IP地址，如果输入为-1，结束输入。

【输出形式】

每行输出一个IP地址在计算机存储中以二进制表示的4字节内容

【样例输入】

192.168.0.1
255.255.0.0
1.0.0.1
-1
【样例输出】

11000000 10101000 00000000 00000001
1111111111111111 0000000000000000
00000001000000000000000000000001'''
# 赖红
# 十进制转换成二进制
def change(n):
    # result = ""
    # while num // 2 != 0:
    #     result += str(num % 2)
    #     num = num // 2
    # print(result)
    # if num != 0:
    #     result += "1"
    # result = result[::-1]
    # print(result)
    result = ""
    while True:
        s = j // 2
        y = j % 2
        result += str(y)
        if s == 0:
            break
        n = s
    result = result[::-1]
    return result.rjust(8, "0")

result = []
while True:
    temp = input()
    if temp == "-1":
        break
    result.append(temp)
for i in result:
    str_temp = [int(s) for s in i.split(".")]
    string = ""
    for j in str_temp:
        string += change(j)
    print(string)