# 例2-3-8  删除空白
favorite_language = 'python '
print('右侧有空格：' + "'" + favorite_language + "'")  #输出加单引号是为了便于看出尾部有空格
print('去除了尾部空格：' + "'" + favorite_language.rstrip() + "'")  #这一步生成了一个新的字符串对象，它的尾部没有空格。
print('favorite_language变量的值未改变：' + "'" + favorite_language + "'")  #原来的字符串对象没有变化

#要永久地删除空白，必须把删除操作的结果存入变量中
favorite_language = favorite_language.rstrip()  #变量favorite_language引用了新的字符串对象
print('favorite_language引用新的字符串：' + "'" + favorite_language + "'")

#lstrip方法删除头部的空白
print('lstrip方法删除头部的空白：')
print('  abc'.lstrip())

#strip方法删除两头的空白
print('strip方法删除两头的空白：')
s1 = '   2 3 4   '
s2 = s1.strip()
print(s2)
