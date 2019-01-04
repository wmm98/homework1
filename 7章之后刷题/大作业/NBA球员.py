print("请输入效率最高的前n个数值：")
n = int(input())
nba_file = open("D:\\The second\\大三上学期\\python\\大作业4及其资料\\大作业4 NBA最佳数据和资料\\player_regular_season.csv")
lines = nba_file .readlines()

del lines[0]
del lines[-1]
del lines[-1]


# 统计各个球员的各项指标
player_efficiency = {}


def to_int(value_str):
    if value_str.strip() == "NULL":
        return 0
    else:
        return int(value_str)


for line in lines:  # [1:]是跳过标题行
    stats = line.split(',')
    ilkid = stats[0].strip()

    # try:
    name = stats[2] + " " + stats[3]
    pts = to_int(stats[8])
    reb = to_int(stats[11])
    asts = to_int(stats[12])
    stl = to_int(stats[13])
    blk = to_int(stats[14])
    fga_fgm = to_int(stats[17]) - to_int(stats[18])
    fta_ftm = to_int(stats[19]) - to_int(stats[20])
    turnover = to_int(stats[15])
    gp = to_int(stats[6])
    efficiency = ((pts + reb + asts + stl + blk) - (fga_fgm + fta_ftm + turnover)) / gp
    if ilkid not in player_efficiency:
        player_efficiency[ilkid] = [efficiency, 1, name]
    else:
        player_efficiency[ilkid][0] += efficiency
        player_efficiency[ilkid][1] += 1

for a, b in player_efficiency.items():
    b[0] = b[0] / b[1]


result_list = list(player_efficiency.items())

def sort_efficiency(x):
    return x[1][0]

result = sorted(result_list, key=sort_efficiency, reverse=True)

print("%34s%16s" % ("姓名", "效率值"))
print("-" * 60)
for i in result[:n]:
    print("%40s%16.0f" % (i[1][2], i[1][0]))

