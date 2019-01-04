#以下为错误比表示方式
'''age = input("请输入你的年龄：");
if age < 30:
    print("你可以进网吧了····");
    '''

#input获取的所有数据，都当做字符串类型，
#所以age为字符串跟18比，没有可比性。

#正确代码
age = input("请输入你的年龄：");
age_num = int(age); #表示为整型
if age_num > 30:
    print("你已经可以进去了");
