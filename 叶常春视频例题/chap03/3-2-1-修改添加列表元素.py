#例3-2-1  修改添加列表元素
#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print(motorcycles)
print("修改第一个元素：")
motorcycles[0] = '嘉陵'
print(motorcycles)

#尾部添加列表元素
print("列表尾部添加元素：")
motorcycles.append('哈雷')
print(motorcycles)

#从空列表开始构造列表
print("从空列表开始：")
bicycles = []
bicycles.append('捷安特')
bicycles.append('永久')
bicycles.append('飞鸽')
print(bicycles)

#向列表中插入元素
print("向列表中插入元素：")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, '哈雷')  #在第1个元素前插入元素
motorcycles.insert(2, '嘉陵')  #在第3个元素前插入元素
print(motorcycles)
