# num = {"name": "李华", "age": 18, "sex": "性别"}
#
# print(num.keys())  # num.keys()表键
# print(num.values())  # num.values()表值
# for temp in num.keys():
#     print(temp)
#
# for temp in num.values():
#     print(temp)
#
# print(num.items())
#
# for a, b in sorted(num.items()):
#     print(a, b)  # 打印字典里每一个整体
#     # age
#     # 18
#     # name
#     # 李华
#     # sex
#     #
# for a, b in num.items():
#     print(a, b)  # 打印字典里每一个整体
# # name 李华
# # age 18
# # sex 性别
# if "sex" in num.keys():
#     print("找到了")

num1 = {"name": 12, "age": 18, "sex": 90}
for i in sorted(num1.values()):
    print(i)