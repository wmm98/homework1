#例6-1-2  字典存储电话簿
contacts = {
    '马云':	'13309283335',
    '赵龙':	'18989227822',
    '张敏':	'13382398921',
    '乔治':	'19833824743',
    '乔丹':	'18807317878',
    '库里':	'15093488129',
    '韦德':	'19282937665'
}

name = input("输入姓名：")
if name in contacts:
    print(name, ":", contacts[name])
else:
    print("没找到" + name)
