"""
问题描述】统计字符串s中非英文字母的个数并输出。

【输入形式】字符串s

【输出形式】非英文字母的个数

【输入示例】a1b2

【输出示例】2

 	"""

s = input()
# print(len(s))
flag = 0
for i in s:
    if not i.isalpha():
        flag += 1
print(flag)
