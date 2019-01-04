

# 分割
name = "wu-89-90-789988"
print(name.split("-"))  # ['wu', '89', '90', '789988']
print(name.split("-", 1))  # ['wu', '89-90-789988'] 1表示分割的次数
print(name)   # wu-89-90-789988


# splitlines()方法语法：
#
# str.splitlines([keepends])
# 参数
# keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
# 返回值
# 返回一个包含各行作为元素的列表。
# 按\n \r分割

name1 = "wu\r89\n90\r789988"
print(name1.splitlines())  # ['wu', '89', '90', '789988']
print(name1.splitlines(True))  # ['wu\r', '89\n', '90\r', '789988']

name = "wu-89-90-789988"
print(name.partition("-"))  # ('wu', '-', '89-90-789988')  从左往右找
print(name.partition("、"))  # ('wu-89-90-789988', '', '')  没有找到的情况下
print(name.rpartition("-"))  # ('wu-89-90', '-', '789988')  从右往做找
print(name.rpartition("、"))  # ('', '', 'wu-89-90-789988')  没有找到的情况下

# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。列表，元组都可用，集合中的中也可以，按照key来找
print("*".join(name))  # w*u*-*8*9*-*9*0*-*7*8*9*9*8*8
print(name)  # wu-89-90-789988 并没有改变原来的字符串