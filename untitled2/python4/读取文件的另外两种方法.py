f_file = open('文件备份.py', encoding="utf-8")
# f = f_file.readlines()
# 打印出来的就是一个列表

f = f_file.readline(10)
# 按字节读出来

# f = f_file.read()
# 一行一行地打印出来
print(f)
f_file.close()
