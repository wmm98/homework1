# 获取要复制的文件名
old_file_name = input("请输入你要备份点的文件名")

# 打开这个文件,读取数据
f = open(old_file_name, "r")

# 创建一个文件 xxx[副件].txt
position = old_file_name.rfind(".")  # 找出点的位置，从右边开始找
str_name = old_file_name[:position]  # 切出mm = str_name
new_file_name = str_name + "[复件].txt"  # 最好改为+'[复件]'+old_file_name[position:]
# print(new_file_name)
b = open(new_file_name, "w", encoding='utf-8')

'''
# 从原文中读取数据，并把数据写入新文件中
f_content = f.read()
b.write(f_content)
'''

# 如果读的文件内存很大，就不可以直接用f.read()去读，应该一部分一部分地去读
while True:
    f_content = f.read(1024)  # 1024个字节，就是一兆地读
    if f_content == 0:
        break

# 关闭两个文件
f.close()
b.close()
