# 例4-1-1  遍历列表
magicians = ['alice', 'david', 'carolina']
# print(magicians)
print("遍历每一个元素：")
for magician in magicians:
    print(magician)

print("元素之前冠以序号：")
index = 1
for magician in magicians:
    print(str(index) + '.', magician)
    index = index + 1
