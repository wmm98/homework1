# 例5-2-9  生词清单
new_words = []
for i in range(1, 101):
    word = input("输入生词：")
    if word == "*":
        break      # break语句的作用是跳出循环，执行循环后面的语句。
    if word not in new_words:
        new_words.append(word)

print("生词清单：", new_words)