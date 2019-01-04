#例10-2-3  追加文件内容

with open("chap10-data/10-2-3-data.txt", "w") as wfile:
    wfile.write("line 1\n")
    wfile.write("line 2\n")
print("文件准备完毕。写入了两行。")
#到with语句之后, 文件已经关闭。

with open("chap10-data/10-2-3-data.txt", "a") as afile:
    afile.write("line 3  appended\n")
    afile.write("line 4  appended\n")
print("文件追加完毕。再写入了两行。")
