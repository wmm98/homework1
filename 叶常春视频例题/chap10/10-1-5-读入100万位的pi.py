#例10-1-5  读入100万位的圆周率
filename = 'chap10-data/pi_million_digits.txt'  #chap10-data和本python文件在同一目录
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

print("上面，圆周率是用字符串存储的。转换为浮点数看看...")
pi = float(pi_string)
print(pi)