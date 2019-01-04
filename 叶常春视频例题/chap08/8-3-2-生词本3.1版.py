#例8-3-2  生词本3.1版
#相比于生词本3.0版，改进了代码结构：
#  1. 利用函数，大幅缩短了用于反复接收命令的while语句的长度。
#  2. 用函数来接收命令输入。
word_dict = {
    'name': '名字',
    'python': '蟒蛇',
    'dictionary': '字典',
    'list': '列表',
    'variable': '变量',
    'class': '类',
    'object': '对象'
}
def read_command():
    '''接收命令'''
    line = input("-->")   # -->是命令提示符
    command = line.split()
    for i in range(0, len(command)):
        command[i] = command[i].strip()  #strip()删除头尾多余的空格
    return command


def append(command, word_dict):
    '''添加生词。没有考虑命令不合法的情形和key重复的情形。'''
    key = command[1]
    value = command[2]
    word_dict[key] = value  # 这里没有考虑key重复的情形
    return "append(" + key + ":" + value + ")  OK."


def delete(command, word_dict):
    key = command[1]
    if key in word_dict:
        del word_dict[key]
        return  "del(" + key + ")  OK."
    else:
        return "No key: " + key + ". Nothing Done."


def query(command, word_dict):
    key = command[1]
    if key in word_dict:
        return key + ": " + word_dict[key]
    else:
        return "No key: " + key


while True:
    #步骤1. 输入命令
    command = read_command()
    #步骤2. 分析命令
    operator = command[0]
    #退出
    if operator == "quit":
        print("bye.")
        break;

    if operator == 'append':
        report = append(command, word_dict)
    elif operator == 'del':
        report = delete(command, word_dict)
    elif operator == 'query':
        report = query(command, word_dict)
    else:
        report = "Bad command: " + operator

    #步骤3. 输出结果
    print(report)
    print(word_dict)
