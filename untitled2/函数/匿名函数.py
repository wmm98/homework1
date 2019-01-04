# 匿名函数

# 第一种表达方式
result = (lambda x, y: x + y)(1, 2)
print(result)  # 3

# 第二种表达
result = lambda x, y: x + y
result1 = result(1, 3)
print(result1)  # 4

# 应用场景
l = [{"name": "wu", "age": 10}, {"name": "you", "age": 78}, {"name": "wo", "age": 67}]
result = sorted(l, key=lambda x: x["age"])
print(result)
# [{'name': 'wu', 'age': 10}, {'name': 'wo', 'age': 67}, {'name': 'you', 'age': 78}]