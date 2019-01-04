"""
【问题描述】

输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
【输入形式】

一个字符串。
【输出形式】

出现次数最多的字母及其出现次数

【样例输入】

abcccd
【样例输出】

c 3
"""

input_str = input()
str_list = []
dic = {}
for i in input_str:
    str_list.append(i)
    d = {i: str_list.count(i)}
    dic.update(d)
#print(dic)

# max_count = max(dic.items(), key=lambda x: x[1])
maxTime = max(dic.values())
#print(maxTime)
#print(dic.values())
a = {}
for item in dic:
    if dic[item] == maxTime:
        a[item] = maxTime
        #print(item, dic[item])
for j in sorted(a.keys()):
    print(j, a[j])




# print(max(dic.items(), key=lambda x: x[1]))
# 这种情况只能求出一个最大值










