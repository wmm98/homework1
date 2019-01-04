#例2-3-7  加号的重载
print(100 + 99)  #整数对象的加法
print(78.0 + 1.0)  #实数的加法

print("Hi" + "," + "everyone.")  #字符串拼接

print("type函数返回对象的类型，也即值的类型。")
score = 100
print(score, ':', type(score))  #int类型 即整数类型
print(888.0, ':', type(888.0))  #float类型，浮点数类型，也即数学上的实数类型
name = "li"
print(name, ':', type(name))   #str类型，即字符串类型

#print函数的新用法：
# print(a, b, c)  -- 输出a，隔一个空格后，输出b，再隔一个空格后，输出c。