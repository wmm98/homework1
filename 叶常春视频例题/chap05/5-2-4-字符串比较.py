#例5-2-4  字符串比较

end_str = input("输入一个字符串：")
if end_str == "end":
    print("输入的是end.")
else:
    print("输入的不是end.")

if end_str > "end":
    print("输入的字符串大于end.")

if end_str < "end":
    print("输入的字符串小于end.")

#啥？Zhong < ba? 字典中不是ba在前？
print("区分大小写比较字符串：")
if "Zhong" < "ba":
    print("Zhong < ba")
else:
    print("Zhong > ba")

#不区分大小写比较字符串
print("不区分大小写比较字符串：")
if "Zhong".upper() < "ba".upper():
    print("Zhong < ba")
else:
    print("Zhong > ba")