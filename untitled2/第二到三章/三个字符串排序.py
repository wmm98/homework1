str1 = input()
str2 = input()
str3 = input()
word = []
word.append(str1)
word.append(str2)
word.append(str3)
# print(word)
word.sort(reverse=True)
for i in word:
    print(i)
