'''
【问题描述】
从键盘中读入最多不超过50个学生的学生信息（包括空格隔开的姓名、学号、年龄信息，以学号从低到高排序）
【输入形式】
每次键盘读入最多不超过50个学生的学生信息：
第一行为学生人数；
后面每一行为空格隔开的学生学号、姓名、年龄，其中学号和年龄都是整数。
【输出形式】
分别以姓名顺序（从低到高）和年龄顺序（从低到高）将学生信息输出，每行输出一位学生的信息，其中学号占3位，
姓名（英文）占6位，年龄占3位，均为右对齐。年龄相同时按姓名从低到高排序。两种顺序的输出结果用一行空行相隔。
【输入样例】
4
1 aaa 20
45 bbb 20
54 ddd 20
110 ccc 20
【输出样例】
     1   aaa     22        
   45    bbb     23      
110      ccc     19 
  54     ddd     20                                      

110     ccc     19        
  54     ddd     20         
    1     aaa     22        
  45     bbb     23                            
【样例说明】
从键盘输入四个学生记录，分别按姓名和年龄排序并输出。
'''
n = int(input())
student_list = []
if n <= 50:

    for r in range(n):
        student_info = []
        s_id, name, age = input().split()
        s_id = int(s_id)
        age = int(age)

        student_info.append(s_id)
        student_info.append(name)
        student_info.append(age)
        student_list.append(student_info)
# print(student_list)

# 按姓名排序
def getKey(x):
    return x[1]

result = sorted(student_list, key=getKey)
for r in range(n):
    # for j in range(3):
    print(str(result[r][0]).rjust(3) + result[r][1].rjust(6) + str(result[r][2]).rjust(3))
print("")

# 按年龄排序
def getKey2(x):

        return x[2]

result2 = sorted(student_list, key=getKey2)
# print(result2)
for i in range(len(result2)):
    for j in range(i + 1, len(result2)):
        if result2[i][2] == result2[j][2] and result2[i][1] > result2[j][1]:
            result2[i], result2[j] = result2[j], result2[i]

# 按年龄排序
for m in range(n):
    print(str(result2[m][0]).rjust(3) + result2[m][1].rjust(6) + str(result2[m][2]).rjust(3))


# n = int(input())
# message = []
# while n > 0:
#     inputList = input().split()
#     message.append(inputList)
#     n -= 1
# print(message)
# def getKeyName(x):
#     return x[1]
# def getKeyAge(x):
#     return x[2]
#
# message = sorted(message, key=getKeyName)
# print(message)
# # 4
# # 1 aaa 22
# # 45 bbb 23
# # 54 ddd 20
# # 110 ccc 20
# for i in message:
#     for j in range(3):
#         if j == 0 or j == 2:
#             print(i[j].rjust(3, " "), end="")
#         else:
#             print(i[j].rjust(6, " "), end="")
#     print()
# print()
# message = sorted(message, key=getKeyAge)
# print(message)
# for i in message:
#     for j in range(3):
#         if j == 0 or j == 2:
#             print(i[j].rjust(3, " "), end="")
#         else:
#             print(i[j].rjust(6, " "), end="")
#     print()











