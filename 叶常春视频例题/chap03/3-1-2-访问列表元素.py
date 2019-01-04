#例3-1-2  访问列表元素
#下标i对应第i+1个元素
bicycles = ['trek', 'cannondale', 'redline', '捷安特', '凤凰', '永久' ]
print(bicycles[0])
print(bicycles[3])

#索引从0开始
print("索引从0开始：")
print(bicycles[1])
#print(bicycles[6])

#倒数的索引
print("倒数的索引：")
print(bicycles[-1])  #最后一个元素
print(bicycles[-2])  #倒数第二个元素
print(bicycles[-3])  #倒数第三个元素

#列表元素的用法与变量完全一样
print("列表元素的用法与变量完全一样:")
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)