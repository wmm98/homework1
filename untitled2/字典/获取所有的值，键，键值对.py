s = {"name": "吴", "sex": "女", "age": 20}
ks = s.keys()
vs = s.values()
it = s.items()
print(ks, vs, it)
# dict_keys(['name', 'sex', 'age']) dict_values(['吴', '女', 20])
# dict_items([('name', '吴'), ('sex', '女'), ('age', 20)])
s['address'] = "佛山市"
print(ks, vs, it)
# dict_keys(['name', 'sex', 'age', 'address']) dict_values(['吴', '女', 20, '佛山市'])
# dict_items([('name', '吴'), ('sex', '女'), ('age', 20), ('address', '佛山市')])

# 可以将他们直接转换为列表或者元组一个一个取出来
ks1 = list(ks)
print(ks1)  # ['name', 'sex', 'age', 'address']

# 通过for循环遍历打印出所有的键
for i in s.keys():
    print(i, end=" ")  # name sex age address

for a, b in s.items():
    print(a, b)
# sex 女
# age 20
# address 佛山市

# 判定
if "吴" in s.values():
    print("找到了")

# 按照 key 来给字典排序：
dict = {200: 'a', 20: 'b', 610: 'c'}

d1 = {}
for k in sorted(dict.keys()):
    d = {k: dict[k]}
    d1.update(d)
print(d1)
# {20: 'b', 200: 'a', 610: 'c'}


