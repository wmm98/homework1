name = "wo shi wu ming ming"
# 查找字符的索引，查到就返回下标，反之返回-1
# 对象.find[str, start , end = len(对象)] [star, end) 起始位置默认是0，结束默认是对象长度
result = name.find("wo")
print(result)

result = name.find("w")  # 在有相同字符情况下只会查找到第一个字符的位置
print(result)

result = name.find("wu")  # 这样找就可以查找到第二个w出现的位置
print(result)

result = name.find("o")
print(result)

# str.refind()也可以查找，只是从右边开始查找索引

# 还可以用 对象.index(str) 来查找目标的索引，用法和find一样，不过查找不到的时候，程序出错

# 计算某个字符出现的次数
# count()方法语法：

# str.count(sub, start= 0,end=len(string))
# 参数
# sub -- 搜索的子字符串
# start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
# end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

# str="www.run oob.com"
# sub='o'
# print ("str.count('o') : ", str.count(sub))
#
# sub='run'
# print ("str.count('run', 0, 10) : ", str.count(sub,0,10)) 起始位置结束位置可以不写
# 以上实例输出结果如下：
#
# str.count('o') :  3
# str.count('run', 0, 10) :  1
