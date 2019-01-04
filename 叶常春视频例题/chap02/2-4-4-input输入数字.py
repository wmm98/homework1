#例2-4-4  输入数字
#输入x，y，输出x+y的和
x = input("输入x：")   #input函数返回的是字符串
y = input("输入y：")
sum = x + y             #两个字符串拼接
print("和：", sum)   #输出拼接得到的字符串

# x = int(x)
# y = int(y)
# sum = x + y
# print("和：", sum)  #输出x+y的和
#
#输入矩形长和宽，求出面积
# fx = float(input("输入矩形宽度："))  #float()函数把字符串转换为浮点数
# fy = float(input("输入矩形长度："))
# print("矩形面积：", fx * fy)