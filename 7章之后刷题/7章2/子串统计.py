'''输入两个字符串，计算字符串二在字符串一中出现的次数。约定：aa字符串在baaab字符串中只算出现一次。

【输入形式】

输入两个字符串，每个字符串一行。其中第一行的字符串为字符串一，第二行为字符串二，即子串。
【输出形式】

按照约定，输出子串在字符串一内出现的次数。
【样例输入】

baaaab
aa
【样例输出】

1'''


father = input().strip()
son = input().strip()
flag = 0

while True:
    if father.find(son) != -1:
        father = father.replace(son, "", 1)
        flag += 1
        # print(father)
    else:
        break
print(flag)