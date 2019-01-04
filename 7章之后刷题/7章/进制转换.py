'''
【问题描述】编写一个程序：将输入的一个N进制整数转换成M进制数（N和M在2到16进制之间），
            要求：N进制数和M进制数均以字符串方式存储。
【输入形式】输入的第一行、第二行分别表示N和M的值，第三行表示需要转换的数值k。
【输出形式】输出的一行为k转换后的结果（超过10的数值依次用大写字母ABCDEF表示，A表示11， B表示12，依次类推），
若输入的进制数值不合法（如：N和M没有落在2到16之间，或数据含有指定进制的非法字符（如：N=2时，k为12）），输出"illegal input"。
【样例输入】
2
16
11000011
【样例输出】
C3
'''

def transfor(x, m):
    transfor_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    new_list = []
    while True:
        a = x // m
        b = x % m
        new_list.append(b)
        if a == 0:
            break
        else:
            x = a
    new_list.reverse()
    final_list = []
    for i in range(len(new_list)):
        final_list.append(transfor_list[new_list[i]])
    return final_list




try:
    num = [2, 8, 10, 16]
    n = int(input())
    m = int(input())
    if n in num and m in num:
        # 将K转为十进制数先
        x = int(input(), n)
        # 调用transfor函数，转为相应的进制
        result = transfor(x, m)
        for j in result:
            print(j, end="")

    else:
        print("illegal input")
except:
    print("illegal input")




