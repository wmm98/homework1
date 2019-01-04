card = [{"name": "lihua", "age": 19}, {"name": "zhangsan", "age": 12}, {"name": "wuhong", "age": 23}]
# 按名字排序
card.sort(key=lambda x: x["name"])
print(card)

# 按年龄大小排序
card.sort(key=lambda x: x["age"])
print(card)

