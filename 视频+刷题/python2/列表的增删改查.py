name = ["李", "陈", "吴", "徐", "赖", "邓", "李"]
name1 = ["小明", "李华", "吴红", "黄华"]

# 增加元素
# 在name1列表的最后增加一个元素
name.append("黄")
print(name)

# 在列表的任意一个地方插元素
name.insert(1, "慕容")
print(name)
name[2] = "司徒"

# 将两个列表合并
names = name + name1
print(names)
name.extend(name1)
print(name)

# 删除元素
# 删除最后一个元素
name.pop()
print(name)

# 随意删除一个元素
name.remove("李")  # 列表中有相同的字符串，只会删除搜索到的第一个
print(name)

name.remove(name[0])
print(name)

# s随意删除
del name[0]
print(name)

# 查询元素
if "李" in name:
    print("找到了")
else:
    print("不在列表中")

if "ming " not in name:
    print("是的")

# 修改元素
name1[0] = "年后"
print(name1)
