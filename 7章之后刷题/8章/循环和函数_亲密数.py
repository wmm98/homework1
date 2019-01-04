'''
【问题描述】

 求整数n以内（含n）的全部亲密数。

说明：如果正整数A的全部因子(包括1，不包括A本身)之和

等于B；且正整数B的全部因子(包括1，不包括B本身)

之和等于A，则将正整数A和B称为亲密数。

1不和其他数形成亲密数。


【输入形式】

输入整数n
【输出形式】

 每一行输出一对亲密数，中间用一个空格隔开。

 每一对亲密数只输出一次，小的在前。

 各对亲密数按序排序，按亲密数中小的那个数从小到大排序。

【样例输入】

3000

【样例输出】

220 284

1184 1210

2620 2924
 	'''

n = int(input())
yin_zi = []
for i in range(220, n + 1):
    yin = [i]
    he = []
    sum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum += j
    yin.append(sum)
    if len(str(i)) == len(str(sum)) and str(i)[0] == str(sum)[0]:  # 降低运行时间
        yin_zi.append(yin)


for o in range(len(yin_zi)):
    for s in range(o + 1, len(yin_zi)):
        if yin_zi[o][0] == yin_zi[s][1] and yin_zi[o][1] == yin_zi[s][0]:
            print(yin_zi[o][0], yin_zi[o][1])

