# 例10-2-1  写入文件
# 调用open()，传入"w"，表示打开文件进行写入。w是write的首字母。
# 如果该文件事先不存在，那么就创建它。
with open("10-2-data.txt", "w") as wfile:
    wfile.write("I love python too.")

print("已经写入10-2-data.txt文件，请检查。")

# print("每次为写入打开已有文件，会清空原有内容，然后写入。")
# with open("10-2-data.txt", "w") as sfile:
#     sfile.write("Wow, Python is a kind of snake.")
