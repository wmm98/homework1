# 例8-4-5  可变对象作为参数
def insert(name, name_list):
    if name not in name_list:
        name_list.append(name)

name_list = []
insert('ye', name_list)
insert('he', name_list)
insert('ye', name_list)
insert('guo', name_list)

print(name_list)