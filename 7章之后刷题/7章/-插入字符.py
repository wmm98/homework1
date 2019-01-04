'''编写一函数insert(string,  c)，用于在一个已排好序（ASCII值从小到大）的字符串string（少于50个字符）中适当位置插入字符c，要求插入后串的序不变（从小到大），允许字符重复，函数返回插入后的字符串。
测试该函数：从键盘分别输入有序字符串和单个字符，然后调用insert函数，并向屏幕输出插入后的字符串。
【输入形式】
从键盘分行输入有序字符串和单个字符
【输出形式】
向屏幕输出插入后的字符串
【输入样例】
abdef   
c   
【输出样例】
abcdef
【样例说明】
从键盘输入少于50个字符的有序字符串abdef和字符c，将字符c插入字符串abdef，并以ASCII值从小到大排序输出'''


def insert(str1, c):
    result_list = [i for i in str1]
    result_list.append(c)
    l = sorted(result_list)
    result = ""
    for j in l:
        result += j
    return result


str1 = input().strip()
c = input().strip()

print(insert(str1, c))
