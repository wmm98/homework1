# 例6-1-1  字典实现生词本
word_dict = {
    'name': '名字',
    'python': '蟒蛇',
    'dictionary': '字典',
    'list': '列表',
    'variable': '变量',
    'class': '类',
    'object': '对象'
}

word = input("输入单词：")
# 下一行检查“word是否在字典中”
if word in word_dict:
    print(word + ":", word_dict[word])
else:
    print("生词本中没有该单词。")
