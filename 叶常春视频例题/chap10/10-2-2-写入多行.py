#例10-2-2  写入多行

with open("10-2-data.txt", "w") as mfile:
    mfile.write("I love python.")
    mfile.write("Python is easy.")
    mfile.write("I love programming.")
print("写入完毕。")

#mfile.write("gogo")  #本行会报错，因为文件已经关闭，不能再写入。

# print("把以上内容写成3行。")
# with open("10-2-data.txt", "w") as sfile:
#     sfile.write("I love python.\n")  #双引号内，两个字符\n一起表示换行符。
#     sfile.write("Python is easy.\n")
#     sfile.write("I love programming.\n")
# print("分3行写入完毕。")