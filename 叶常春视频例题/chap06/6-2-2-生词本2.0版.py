# 例6-2-2  生词本2.0版
word_dict = {
    'name': '名字',
    'python': '蟒蛇',
    'dictionary': '字典',
    'list': '列表',
    'variable': '变量',
    'class': '类',
    'object': '对象'
}

# 步骤1. 输入命令
line = input("-->")   # -->是命令提示符
command = line.split()
for i in range(0, len(command)):
    command[i] = command[i].strip()  # strip()删除头尾多余的空格

# 步骤2. 分析命令
operator = command[0]
if operator == 'append':
    key = command[1]
    value = command[2]
    word_dict[key] = value  # 这里没有考虑key重复的情形
    result = "append(" + key + ":" + value + ")  OK."

if operator == 'del':
    key = command[1]
    if key in word_dict:
        del word_dict[key]
        result = "del(" + key + ")  OK."
    else:
        result = "No key: " + key + ". Nothing Done."

if operator == 'query':
    key = command[1]
    if key in word_dict:
        result = key + ": " + word_dict[key]
    else:
        result = "No key: " + key

# 步骤3. 输出结果
print(result)
print(word_dict)

# 2.0版只能接收处理一条命令。3.0版将支持反复输入命令。