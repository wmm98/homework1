#例10-1-3  逐行读取

with open("10-1-data.txt") as datafile:
    for line in datafile:  #逐行读取
        print(line)

print("上面的输出，行与行之间有一行空白。"
      "原因是除了最后一行，读入的各行结尾有换行符。加上print()本身会换行。")
print("下面的输出不隔开一行空白。")
with open("10-1-data.txt") as datafile:
    for line in datafile:
        print(line.rstrip())  #rstrip()删除尾部空白（含换行符、制表符和空格）
