num = input().strip()
# num4 = num.isdigit()  # 判断字符串内是否全为数字
str = "-"
str_count = num.count(str)
# print(str_count)
if str_count >= 2:
    print("no")
elif str_count == 1:
    if num.index(str) == 0 and num.lstrip(str).isdigit():
        print("yes")
    else:
        print("no")
else:
    if num.isdigit():
        print("yes")
    else:
        print("no")


# strInput = input().strip()
# num = strInput.count("-")
# temp = strInput.lstrip("-")
# if strInput.isdigit() or num == 1 and temp.isdigit():
#     print("yes")
# else:
#     print("no")