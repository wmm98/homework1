'''键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。找出姓、
名字或电子邮箱地址中有"Li"或"li"出现的雇员，输出这些雇员的信息。

【输入形式】
从键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。雇员信息之间隔有一行空白。
【输出形式】
输出姓、名字或电子邮箱地址中有"Li"或"li"出现的雇员的信息。雇员信息之间空一行。
【样例输入】
zhang
san
zhangsan@hotmail.com
nudt

li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt

zhao
zao
zhaozaoLIU@163.com
nudt

qian
qi
qianqi@163.com
nudt
【样例输出】

li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt 	
'''

all_information = []
count = 0
for i in range(5):
    # count += 1
    # if count != 0:
    #     print("")
    information = {}
    new_name = input()
    new_name1 = input()
    new_email = input()
    new_address = input()
    if i != 4:
        line = input()

    information["f_name"] = new_name
    information["g_name"] = new_name1
    information["email"] = new_email
    information["address"] = new_address
    all_information.append(information)
    # print("\n")

# print(all_information)
flag = 0
for temp in all_information:
        if ("li" == temp["f_name"]) or ("Li" == temp["f_name"]) or ("li" == temp["f_name"]) or\
                ("Li" == temp["f_name"]) or ("Li" in temp["email"]) or ("li" in temp["email"]):
        # if ("Li" or "li") == (temp["f_name"] or temp["g_name"]) or (("Li" or "li") in temp["email"]):
            flag += 1
            if flag != 1:
                print("")
            print("%s" % temp["f_name"])
            print("%s" % temp["g_name"])
            print("%s" % temp["email"])
            print("%s" % temp["address"])
            # print("\n")

