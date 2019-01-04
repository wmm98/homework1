#例7-2-15  求多个分数的平均分
#功能：输入多个分数，求出平均分。如果输入的分数小于0或大于100，则丢弃。
#  输入-1表示输入结束。

sum = 0
count = 0
while True:
    score = int(input("输入分数（-1表示结束）："))
    if score == -1:
        break

    if score < 0 or score > 100:
        print("分数不合法，丢弃：", score)
        continue

    sum += score
    count += 1

if count > 0:
    avg = sum / count
    print("平均分：", avg)
else:
    print("没有有效的输入。")