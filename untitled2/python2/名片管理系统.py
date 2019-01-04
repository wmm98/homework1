# 名片管理系统
print("=" * 55)
print("1.添加用户信息")
print("2.删除用户信息")
print("3.查找用户信息")
print("4.修改用户信息")
print("5.打印所有用户信息")
print("6.退出系统")

# 名片管理系统是在列表中嵌套字典
# 创建列表
card_infor = []
flag = 0  # 默认为没有找到

while True:
    num = int(input("请输入序号"))
    if num == 1:
        new_name = input("请输入你的姓名")
        new_age = int(input("请输入你的年龄"))
        new_sex = input("请输入你的性别")
        new_WeChat = input("请输入你的微信号")

        # 创建词典
        infor = {}
        infor["name"] = new_name
        infor["age"] = new_age
        infor["sex"] = new_sex
        infor["WeChat"] = new_WeChat
        print(infor)
        card_infor.append(infor)
        print(card_infor)
    elif num == 2:
        delete_name = input("请输入你要删除的名字")
        for temp in card_infor:
            if delete_name == temp["name"]:
                card_infor.remove(temp)
                print(card_infor)
                flag = 1
                print("mmmm")
                break
        if flag == 0:
            print("查无此人")

    elif num == 3:
        find_name = input("输入你要查找的名字")
        for temp in card_infor:
            if find_name == temp["name"]:
                print("%s,%d，%s,%s" % (temp["name"], temp["age"], temp["sex"], temp["WeChat"]))

                # for循环里最好不要嵌套else,很容易出错

                flag = 1  # 表示找到了
                break  # 跳出for循环
        if flag == 0:
            print("没有此人")
            # else:当break执行的时候else就不执行，如果break不执行的时候，else执行，也可用这种方法
            # print("没有此人")

    elif num == 4:
        change_name = input("请输入你要修改的名字")
        for temp in card_infor:
            if change_name == temp["name"]:
                new_name = input("请输入新的名字")
                new_WeChat = input("请输入新的微信号")
                new_age = input("请输入新的年龄")
                new_sex = input("请输入新的性别")
                temp["name"] = new_name
                temp["age"] = new_age
                temp["sex"] = new_sex
                temp["WeChat"] = new_WeChat
                print(card_infor)
                flag = 1
                break
        if flag == 0:
            print("无此人")
    elif num == 5:
        print("名字\t年龄\t性别\t微信号")
        for temp in card_infor:
            print("%s\t%d\t%s\t%s" % (temp["name"], temp["age"], temp["sex"], temp["WeChat"]))
    elif num == 6:
        break
