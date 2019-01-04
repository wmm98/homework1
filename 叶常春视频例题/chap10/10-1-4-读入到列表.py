# 例10-1-4  读入到列表
filename = 'chap10-data/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # readlines()一次性地读入所有行。每一行作为一个元素存入列表中。
    print(lines)

pi_string = ''
for line in lines:
    pi_string += line.rstrip()  # 删除右侧空白
print(pi_string)
print(len(pi_string))

print("删除两侧空白的输出...")
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
