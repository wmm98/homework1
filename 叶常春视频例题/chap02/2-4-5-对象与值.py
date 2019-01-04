#例2-4-5  对象与值
#Python程序中，每一个值都用一个对象来存储。
hi = "Hi, everyone."   #这一语句会生成字符串对象。
print("字符串对象的类型：", type(hi))
n = 123  #生成整数对象
print("整数对象的类型：", type(n))
f = 5.6  #生成浮点数对象
print("浮点数对象的类型：", type(f))

#id()函数返回对象的id
print("字符串对象的id:")
print(id(hi))
print("整数对象的id:")
print(id(n))
print("浮点数对象的id:")
print(id(f))

#dir()函数返回对象的属性
print("字符串对象的属性：")
print(dir(hi))
print("整数对象的属性：")
print(dir(n))
print("浮点数对象的属性：")
print(dir(f))
