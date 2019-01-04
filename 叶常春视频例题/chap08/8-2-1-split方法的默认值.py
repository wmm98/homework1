#例8-2-1  split方法的默认值

#字符串对象的split方法有两个参数：str.split(sep=None, maxsplit=-1)
#第一个参数sep用于指定分隔符。默认值是None，意味着以空格类字符作为分隔符。
#第二个参数maxsplit用于指定分割多少项。默认值是-1，意味着分割所有项。
print("空格类字符（如空格、制表符(\t)、换行符(\n)）作为分隔符：")
print((' 1\t 2   3').split())  #等同于split(sep=None, maxsplit=-1)
print((' 1\t 2   3').split(None))
print('1 2 3'.split(maxsplit=1))   #只分割一项
print(('1\n2\t3').split())

print("逗号作为分隔符：")
print('1,2,3'.split(','))
print('1,2,3, 5'.split(',', maxsplit=2))  #分割两项

