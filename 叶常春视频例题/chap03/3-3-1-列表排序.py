#例3-3-1  对列表进行排序
# sort()方法的用法
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print("排序前：", motorcycles)
motorcycles.sort()  #调用形式是：对象.方法名()
print("排序后：", motorcycles)

print("逆向排序前：", motorcycles)
#下一行调用sort()方法，传递了一个参数。
#sort()方法一共有2个参数，写法是sort(key, reverse)
#  第一个参数key是一个函数，用于生成比较用的键。如果为空(None）,则直接拿列表元素的值进行比较。
#  第二个参数reverse设为True时，意味着进行逆向排序；为False时，是正向排序。
motorcycles.sort(reverse=True)
# 上一行中，参数的写法值得注意。reverse=True，是指本次调用传给reverse参数的值为True。
#上述写法叫关键字参数。
print("逆向排序后：", motorcycles)

# sorted()函数的用法
motorcycles = ['宗申', 'honda', 'yamaha', 'suzuki', '钱江']
print("调用sorted()函数之前，列表内容：", motorcycles)
result = sorted(motorcycles)
print("调用sorted()函数之后，列表内容：", motorcycles)
print("调用sorted()函数之后，排序结果：", result)

#利用sorted()函数进行逆向排序
nx = sorted(motorcycles, reverse=True)
print("调用sorted()函数，进行逆向排序：", nx)
