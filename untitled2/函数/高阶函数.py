# 当一个函数A接收的参数时另外一个函数时，则称其为高阶函数
l = [{"name": "wu", "age": 10}, {"name": "you", "age": 78}, {"name": "wo", "age": 67}]


def getKey(x):
    # return x["name"]  # x代表接收的一个元素
    return x["age"]
    # [{'name': 'wu', 'age': 10}, {'name': 'wo', 'age': 67}, {'name': 'you', 'age': 78}]


result = sorted(l, key=getKey)
print(result)
# [{'name': 'wo', 'age': 67}, {'name': 'wu', 'age': 10}, {'name': 'you', 'age': 78}]

