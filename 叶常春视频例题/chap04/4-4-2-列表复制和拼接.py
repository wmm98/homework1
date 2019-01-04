# 例4-4-2  列表复制和拼接
# 引用复制
players = ['charles', 'martina', 'michael', '马龙', '孙杨']
print("1. players=", players)
plist = players  # 引用复制：plist是players列表的另一个名字
plist.append('姚明')
print("2. players=", players)

# 内容复制
players = ['charles', 'martina', 'michael', '马龙', '孙杨']
print("3. players=", players)
plist = players[:]
# print(plist)  复制3的列表
plist.append('姚明')
print("4. players=", players)
print("5. plist=", plist)

# 列表拼接
my_foods = ['pizza', 'rice', 'milk']
your_foods = ['口味虾', '红烧肉', '馒头']
foods = my_foods + your_foods
print("6. foods=", foods)
your_foods[0] = '剁椒鱼头'
print("7. foods=", foods)
