
f_file = open("mm[复件].txt", 'r+', encoding="utf-8")
f_file.write("我正在带代码啊啊 啊啊啊啊啊你好啊")
print(f_file.tell())
f_file.seek(5, 0)
print(f_file.read())
f_file.close()


