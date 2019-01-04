#例8-6-3  生词本3.2版
#相比于生词本3.1版，使用了模块：
#  1. 把子函数移到newWordsFuncs模块

import  newWordsFuncs as nwf

word_dict = {
    'name': '名字',
    'python': '蟒蛇',
    'dictionary': '字典',
    'list': '列表',
    'variable': '变量',
    'class': '类',
    'object': '对象'
}

while True:
    #步骤1. 输入命令
    command = nwf.read_command()
    #步骤2. 分析命令
    operator = command[0]
    #退出
    if operator == "quit":
        print("bye.")
        break;

    if operator == 'append':
        result = nwf.append(command, word_dict)
    elif operator == 'del':
        result = nwf.delete(command, word_dict)
    elif operator == 'query':
        result = nwf.query(command, word_dict)
    else:
        result = "Bad command: " + operator

    #步骤3. 输出结果
    print(result)
    print(word_dict)
