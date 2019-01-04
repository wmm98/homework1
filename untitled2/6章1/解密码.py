'''
有一行电文，已按下面规律译成密码：

     A--Z   a--z
     B--Y   b--y

     C--X   c--x

     ......

即第1个字母变成第26个字母，第i个字母变成第（26-i+1）个字母; 非字母字符不变。编写程序把密码译回原文，并输出密码和原文。

【输入形式】

输入一串密码（长度为10，可包含数字、字母）

【输出形式】

首先输出密码，然后换行后输出原文

【样例输入】

4sdf&13TBD

【样例输出】

4sdf&13TBD

4hwu&13GYW

'''

upper_eng = [chr(i) for i in range(65, 91)]
upper_eng1 = upper_eng[::-1]
lower_eng = [chr(i).lower() for i in range(65, 91)]
lower_eng1 = lower_eng[::-1]


mima = input()

result = ""
for j in mima:
    if j.isalpha():

        if j.isupper():
            j_index = upper_eng.index(j)
            result += upper_eng1[j_index]
        else:
            j_index = lower_eng.index(j)
            result += lower_eng1[j_index]
    else:
        result += j
print(mima)
print(result)

