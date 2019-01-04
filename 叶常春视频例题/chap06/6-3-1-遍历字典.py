# 例6-3-1  遍历字典
contacts = {
    '马云': '13309283335',
    '赵龙': '18989227822',
    '张敏': '13382398921',
    '乔治': '19833824743',
    '乔丹': '18807317878',
    '库里': '15093488129',
    '韦德': '19282937665'
}

# 遍历键值对
print("全部键值对：")
for k, v in contacts.items():
    print(k, ':', v)

# 遍历键
print("\n全部键：")  # \n造成输出换行
for key in contacts.keys():
    print(key)

# 遍历值
print("\n全部值：")
for value in contacts.values():
    print(value)
