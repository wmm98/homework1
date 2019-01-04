#例10-1-6  圆周率包含你的生日吗
filename = 'chap10-data/pi_million_digits.txt'  #chap10-data和本python文件在同一目录
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday_string = input("输入你的生日(mmddyy)：")
if birthday_string in pi_string:
    print("你的生日出现在圆周率中。")
else:
    print("你的生日没有出现在圆周率中。")