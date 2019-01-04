#例5-3-1
age = int(input("输入年龄："))
if age < 4:
    price = 0
elif age < 18:    #elif来自else if
    price = 5
else:
    price = 10
print("票价(元）：", price)

