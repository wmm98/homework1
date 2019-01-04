"""
【问题描述】从若干学生成绩中统计高于(严格的大于)平均分的人数，用-1做为学生成绩数据的结束标志
【输入形式】一组学生的成绩
【输出形式】高于平均分的学生人数
【样例输入】70 50 80 -1
【样例输出】2
"""

score = input().split()
score1 = score[:-1]
# print(score1)
sum = 0
score2 = []
for i in score1:
    i = int(i)
    score2.append(i)
    sum += i
if len(score2) != 0:
    avg = sum / len(score2)
flag = 0
for j in score2:
    if j > avg:
        flag += 1
print(flag)