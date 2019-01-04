str = input("")
str1 = str.strip()  # 去掉首尾空格
str4 = str1.isalpha()  # 判断字符串内是否全为字母

if str4:
    print("yes")
else:
    print("no")
