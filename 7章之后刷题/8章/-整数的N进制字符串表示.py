'''编写函数itob(n,b),用于把整数n转换成以b为基底的字符串并返回.   

编写程序,使用函数itob(n,b)将输入的整数n,转换成字符串s,将s输出。转换后的字符串从最高的非零位开始输出。如果n为负数，
则输出的字符串的第一个字符为'-'。b为大于1小于37的任意自然数。当b=2时，输出字符只可能是'0'和'1'；当b=16时，
输出字符串中可能含有字符为'0'-'9'，'a'-'f'(字母以小写输出)。b为18时，数码是'0'-'9'，'a'-'h'，
其中'a'代表10，'g'代表16， 'h'代表17。又比如，输入n=33,b=17，则输出33的17进制值为"1g"。

【输入形式】输入整数n和b，其中n可以为负数。n和b以空格分隔.
【输出形式】输出转换后的字符串s.
【样例输入】5 2
【样例输出】101
【样例说明】5的二进制就是101'''


def f(n, x):

    list1 = [i for i in range(10)]
    list2 = [chr(j).lower() for j in range(65, 91)]
    a = list1 + list2
    b_list = []
    while True:
        s = n // x
        # print(s)
        y = n % x
        b_list.append(y)
        if s == 0:
            break
        n = s
    b_list.reverse()
    # print(b)
    c = []
    for i in range(len(b_list)):
        c.append(a[b_list[i]])

    # for j in c:
    #     if j == 0:
    #         c.remove(j)
    #         break
    #     else:
    #         break

    if c[0] == 0:
        return c[1:]
    else:
        return c

n1, b = input().split()
if int(n1) >= 0:
    result = f(int(n1), int(b))
else:
    result = f(int(n1[1:]), int(b))
    result.insert(0, "-")
for i in result:
    print(i, end="")
