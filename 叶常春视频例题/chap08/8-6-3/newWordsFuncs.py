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

