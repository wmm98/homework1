print("请输入值n")
n = int(input())
nba_file = open("D:\\The second\\大三上学期\\python\\大作业4及其资料\\大作业4 NBA最佳数据和资料\\player_regular_season.csv")
lines = nba_file .readlines()
del lines[0]
del lines[-1]
del lines[-1]

# minute = 0
# pg = 0
# pts = 0
# reb = 0
# fta = 0
# ftm = 0

# 处理数据


def to_int(value_str):
    if value_str.strip() == "NULL":
        return 0
    else:
        return int(value_str)

dic = {}
for line in lines:
    new_line = line.split(",")
    name = new_line[2] + " " + new_line[3]
    if new_line[0].strip() not in dic:
        dic[new_line[0].strip()] = [name, to_int(new_line[6]), to_int(new_line[7]), to_int(new_line[8]), to_int(new_line[11]),
                                    to_int(new_line[19]), to_int(new_line[20])]
    else:
        dic[new_line[0].strip()][1] += to_int(new_line[6])
        dic[new_line[0].strip()][2] += to_int(new_line[7])
        dic[new_line[0].strip()][3] += to_int(new_line[8])
        dic[new_line[0].strip()][4] += to_int(new_line[11])
        dic[new_line[0].strip()][5] += to_int(new_line[19])
        dic[new_line[0].strip()][6] += to_int(new_line[20])

    # pg += to_int(new_line[6])
    # minute += to_int(new_line[7])
    # pts += to_int(new_line[8])
    # reb += to_int(new_line[11])
    # fta += to_int(new_line[19])
    # ftm += to_int(new_line[20])

result_list = list(dic.items())
list2 = ["pg:", "minute:", "pts:", "reb:", "fta:", "ftm:"]


# def max_men(x):
#     return x[1][1]
# result = sorted(result_list, key=max_men, reverse=True)
# print(result)
for i in range(1, len(list2) + 1):
    def max_men(x):
        return x[1][i]
    result = sorted(result_list, key=max_men, reverse=True)
    for j in result[:n]:
        print(list2[i - 1] + j[1][0])