#例10-2-4  写入汉字
print("下面的写法，将向文件写入gbk编码的汉字。")
with open("chap10-data/10-2-4.txt", "w") as wfile:
    wfile.write("我喜欢Python\n")
    wfile.write("我喜欢编程。\n")

import codecs
print("下面的写法，将向文件追加utf-8编码的汉字。")
with codecs.open("chap10-data/10-2-4.txt", "a", "utf-8") as afile:
    afile.write(u"我喜欢Python\n")
    afile.write(u"我喜欢编程。\n")