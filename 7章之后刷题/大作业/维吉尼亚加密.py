'''
莱瑟·维吉尼亚将凯撒密码做了推广。维吉尼亚加密使用的秘钥是一串文本，比如“LEMON”。下面以“LEMON”作秘钥，
 “ATTACKATONECLOCK” 作明文为例，阐述维吉尼亚加密方法。
1.水平平铺明文和秘钥，如表1第一，二行所示。从第二行可以看到，秘钥被重复使用。
表1 维吉尼亚密码表
明文	A	T	T	A	C	K	A	T	O	N	E	C	L	O	C	K
秘钥	L	E	M	O	N	L	E	M	O	N	L	E	M	O	N	L
密文	L	X	F													
2.明文第一个字母的加密：它对应的秘钥字母是L，计算L与字母表首字母（即A）的距离，
得到11。以该距离值作为秘钥，对第一个字母A实施凯撒加密，得到密文字母L。
3.明文第二个字母的加密：它对应的秘钥字母是E，计算E与字母表首字母（即A）的距离，
得到4。以该距离值作为秘钥，对第二个字母T实施凯撒加密，得到密文字母X。
4.明文第三个字母的加密：它对应的秘钥字母是M，计算M与字母表首字母（即A）的距离，
得到12。以该距离值作为秘钥，对第三个字母T实施凯撒加密，得到密文字母F。
5.以此类推，可得到明文后续字母的密文字母。


题2  维吉尼亚加密
编写维吉尼亚加密程序，输入秘钥key和明文，输出密文。说明一点：
如果秘钥字母为大写字母，则以该字母与大写A字母的距离作为凯撒加密秘钥；
若秘钥字母为小写，则以该字母与小写a字母的距离作为凯撒加密秘钥。

LEMON
ATTACKATONECLOCK
'''


# 生成字母表
upper_list = [chr(i) for i in range(65, 91)]
lower_list = [chr(i).lower() for i in range(65, 91)]
upper_list = upper_list + upper_list
lower_list = lower_list + lower_list

key = input()
word = input()
length1 = len(word) // len(key)
length2 = len(word) % len(key)
# 秘钥
key1 = key * length1 + key[:length2]

result = ""
word_index = upper_list.index(word[0].upper())
for i in range(len(key1)):
    key1_index = upper_list.index(key1[i].upper())
    word_index1 = upper_list.index(word[i].upper())
    # print(key1_index)
    length3 = abs(word_index - key1_index)
    if word[i].isupper():
        result += upper_list[word_index1 + length3]
    elif word[i].islower():
        result += lower_list[word_index1 + length3]
    else:
        result += word[i]
print(result)


