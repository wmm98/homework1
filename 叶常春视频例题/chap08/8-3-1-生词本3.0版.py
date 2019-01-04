#例8-3-1  生词本3.0版
#相比于生词本2.0版，增加了以下功能：
#  1. 反复地接收用户的命令
#  2. 不支持的操作，会报告“Bad command”
word_dict = {
    'name': '名字',
    'python': '蟒蛇',
    'dictionary': '字典',
    'list': '列表',
    'variable': '变量',
    'class': '类',
    'object': '对象'
}


def append():
    global key, result
    key = command[1]
    value = command[2]
    word_dict[key] = value  # 这里没有考虑key重复的情形
    result = "append(" + key + ":" + value + ")  OK."
    return result


def delete():
    global key, result
    key = command[1]
    if key in word_dict:
        del word_dict[key]
        result = "del(" + key + ")  OK."
    else:
        result = "No key: " + key + ". Nothing Done."
    return result


def query():
    global key, result
    key = command[1]
    if key in word_dict:
        result = key + ": " + word_dict[key]
    else:
        result = "No key: " + key
    return result


while True:
    #步骤1. 输入命令
    line = input("-->")   # -->是命令提示符
    command = line.split()
    for i in range(0, len(command)):
        command[i] = command[i].strip()  #strip()删除头尾多余的空格
    #退出
    if command[0] == "quit":
        print("bye.")
        break;

    #步骤2. 分析命令
    operator = command[0]
    if operator == 'append':
        result = append()
    elif operator == 'del':
        result = delete()
    elif operator == 'query':
        result = query()
    else:  #非法命令
        result = "Bad command: " + operator

    #步骤3. 输出结果
    print(result)
    print(word_dict)

#上述代码，while语句块过长了。导致代码可读性不强。
#改进措施：用函数实现若干子步骤，缩短while语句的长度。见生词本3.1版。