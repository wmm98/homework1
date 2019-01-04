#10-1-2  文件路径

print("通过相对路径访问文件。路径的起点是本python文件所在的目录。")
with open("chap10-data/10-1-2-files.txt") as f_file:
    contents = f_file.read()
print(contents)

print("通过绝对路径访问文件。绝对路径的起点是盘符。")
#下面的绝对路径，需要根据10-1-2-files.txt文件在你的电脑外存上的位置，作出修改，否则会报错。
with open(r"C:\Users\612226\PycharmProjects\pythonSamples\tutorialExamples\chap10\chap10-data\10-1-2-files.txt") as a_file:
            #字符串前面的r表明，紧跟其后的字符串是无须转义的原始字符串。就本例而言，意味着反斜杠是元素，不是转义符号。
            #去掉左侧的r字符的话，那么所有的反斜杠（\)要写作两个反斜杠（\\），否则会报错。你可以试一试看看。
    contents = a_file.read()
print(contents)