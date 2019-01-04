# 输入数值，不考虑下非数字
num = int(input())

# 判断是否是三位数
if 100 <= num < 1000:
    num = num
else:
    print("输入不对，直接退出")
    exit()


# 判断是是否为水仙花数
# 水仙花数：xyz = x ** 3 + y ** 3 + z ** 3
# 取百位数，十位数，个位数
bw = num // 100
# print(bw)
sw = num % 100 // 10
# print(sw)
gw = num % 100 % 10
if bw ** 3 + sw ** 3 + gw ** 3 == num:
    print("你猜对")
else:
    print("你猜错了")

