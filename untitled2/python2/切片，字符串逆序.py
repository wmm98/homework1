name = "wumingMING"
print(name[2:4])  # 其中2表示字符串数组的下标，4表示原来的位置的第几位，可表示为【起始位置:终止位置】'''
print(name[2:-1])  # 表示数组下标第二个数到倒数第二个数
print(name[0:])  # 表示整列数

print(name[2:-1:2])  # 输出的结果为m n m n就是每隔两步取字母，课表示为变量名【起始位置：终止位置：步数】

print(name[-1:0:-1])  # 第三个-1表示逆序走，然而输出的结果逆序不全，缺少一个W,也就是逆序的最后一个
print(name[-1::-1])  # 输出的是整个字符串的逆序
print(name[::-1])  # 输出的也是整段字符串的逆序
# 第一个冒号前后不写表明默认系统会按照顺序来搜索
