# 【问题描述】去掉字符串s中的指定字符，并将新得到的字符串输出。
# 【输入形式】一个字符串，和要去掉的字符（两者中间有一个空格）
# 【输出形式】去掉特定字符后的新字符串
# 【样例输入】abdsag d
# 【样例输出】absag
# 【样例说明】要去除指定字符的全部出现

str1, str2 = input().split()
list1 = []

for j in str1:
    list1.append(j)
list1.remove(str2)
count = ""
for i in list1:
    count += i
print(count)






