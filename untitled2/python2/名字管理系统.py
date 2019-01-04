print("===名字管理系统===")
print("===1.添加姓名===")
print("===2.删除姓名===")
print("===3.查询姓名===")
print("===4.修改姓名")
print("===5.退出")

name = []#该列表只执行一遍，所以要在while循环外面

while True:
    num = int(input("请输入序号"))
    if num == 1:
        new_names = input("请输入你的名字")
        name.append(new_names)
        print(name)
    if num == 2:
        Delete_name = input("请输入你要删除的名字")
        name.remove(Delete_name)
        print(name)
    if num == 3:
        Check_name = input("请输入你要查询的名字")
        if Check_name in name:
            print("找到了")
        else:
            print("没有该名字")
    if num == 4:
        name[0] = "橙红"
        print(name)
    if num == 5:
        break