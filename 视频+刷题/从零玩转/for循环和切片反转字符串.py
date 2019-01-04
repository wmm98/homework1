word = "社会我明姐，人狠话不多"
# 设置一个空字符串累加存储
result = ""
for i in word:
    # result += i # 按顺序遍历出来
    result = i + result  # 逆序遍历
print(result)


word1 = word[::-1]
print(word1)