#例3-2-2 删除列表元素
# del语句删除列表元素
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print(motorcycles)
print("删除第一个元素：")
del motorcycles[0]
print(motorcycles)
print("删除第三个元素：")
del motorcycles[2]
print(motorcycles)
#del 'suzuki'   #这样写是错误的。


#pop()方法删除列表尾部元素
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print("pop()方法删除尾部元素。开始列表是：",motorcycles)
print("第一次pop():")
qj = motorcycles.pop()
print(motorcycles)
print("被删除的元素：", qj)
print("第二次pop():")
zs = motorcycles.pop()
print(motorcycles)
print("被删除的元素：", zs)

#pop(i)删除第i+1个元素
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print("pop(i)方法删除第i+1个元素。一开始，列表是：",motorcycles)
print("pop(0)之后：")
honda = motorcycles.pop(0)
print(motorcycles)
print("被删除的元素是：", honda)
print("再pop(2)之后：")
zs = motorcycles.pop(2)
print(motorcycles)
print("被删除的元素是：", zs)

#remove(value)删除值为value的元素
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print("remove(v)方法删除值为v的元素。一开始，列表是：", motorcycles)
print("remove('honda')之后：")
motorcycles.remove('honda')
print(motorcycles)

