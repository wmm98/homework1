nba_stastics_file = open("D:\\The second\\大三上学期\\python\\大作业4及其资料\\大作业4 NBA最佳数据和资料\\player_regular_season.csv")
lines = nba_stastics_file.readlines()

# 去除最后两行
del lines[-1]
del lines[-1]

# print(lines[0], end="")
# for line in lines:
#     if "James" in line:
#         print(line, end="")
# print(lines[-1])

# 统计ilkid=YoungTh01这个球员的上场时间
# sum_minutes = 0
# for line in lines:
#     stats = line.split(',')
#     if "YoungTh01" == stats[0].strip():
#         print(stats)
#         sum_minutes += int(stats[7])
#
# print("YoungTh01的上场时间：", sum_minutes)


# 统计各个球员的各项指标
player_efficiency = {}


def to_int(value_str):
    if value_str.strip() == "NULL":
        return 0
    else:
        return int(value_str)


for line_no, line in enumerate(lines[1:]):  # [1:]是跳过标题行
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
        player_efficiency[ilkid] = [efficiency, 1]
    else:
        sum_efficiency, count = player_efficiency[ilkid]
        player_efficiency[ilkid] = [sum_efficiency + efficiency, count + 1]
    # except ValueError as ve:
    #     print("line NO: ", line_no + 2)
    #     print(line)
    #     exit(0)
# for j in player_efficiency.values():
#     print(j)

# print("YoungTh01的上场时间：", player_minutes['YoungTh01'])
for ilkid in player_efficiency:
    sum_efficiency, count = player_efficiency[ilkid]
    player_efficiency[ilkid] = sum_efficiency / count

# for j in player_efficiency.values():
#     print(j)

player_efficiency_list = list(player_efficiency.items())

# for i in player_efficiency_list:
#     print(i)

player_efficiency_list.sort(key=lambda p_m: p_m[1], reverse=True)

n = int(input("对于效率值，你要输出前多少位？\n"))
if n <= 0:
    print("输入不合法！")
    exit(0)

id_names = {}
for line_no, line in enumerate(lines[1:]):  # [1:]是跳过标题行
    stats = line.split(',')
    ilkid = stats[0].strip()
    if ilkid not in id_names:
        id_names[ilkid] = stats[2] + " " + stats[3]

print("%40s%16s" % ("姓名", "效率值"))
print("-" * 66)
for i in range(n):
    print("%40s%16.0f" % (id_names[player_efficiency_list[i][0]], player_efficiency_list[i][1]))

# 另一种计算方法----把各个赛季的数据合计在一起，然后计算
player_stats = {}
for line_no, line in enumerate(lines[1:]):  # [1:]是跳过标题行
    stats = line.split(',')
    ilkid = stats[0].strip()
    try:
        # name = stats[2] + " " + stats[3]
        pts = to_int(stats[8])
        reb = to_int(stats[11])
        asts = to_int(stats[12])
        stl = to_int(stats[13])
        blk = to_int(stats[14])
        fga_fgm = to_int(stats[17]) - to_int(stats[18])
        fta_ftm = to_int(stats[19]) - to_int(stats[20])
        turnover = to_int(stats[15])
        gp = to_int(stats[6])
        # efficiency = ((pts + reb + asts + stl + blk) - (fga_fgm + fta_ftm + turnover)) / gp
        if ilkid not in player_stats:
            player_stats[ilkid] = [pts, reb, asts, stl, blk, fga_fgm, fta_ftm, turnover, gp]
        else:
            tpts, treb, tasts, tstl, tblk, tfga_fgm, tfta_ftm, tturnover, tgp = player_stats[ilkid]
            player_stats[ilkid] = [pts + tpts, reb + treb, asts + tasts, stl + tstl,
                                   blk + tblk, fga_fgm + tfga_fgm, fta_ftm + tfta_ftm, turnover + tturnover, gp + tgp]
    except ValueError as ve:
        traceback.print_exc()
        print("正在处理的数据行是: ", line_no + 2)
        print(line)
        exit(0)

player_efficiency = {}
for ilkid in player_stats:
    tpts, treb, tasts, tstl, tblk, tfga_fgm, tfta_ftm, tturnover, tgp = player_stats[ilkid]
    player_efficiency[ilkid] = ((tpts + treb + tasts + tstl + tblk) - (tfga_fgm + tfta_ftm + tturnover)) / tgp

player_efficiency_list = list(player_efficiency.items())
player_efficiency_list.sort(key=lambda p_m: p_m[1], reverse=True)
print("\n另一种算法：")
print("%40s%16s" % ("姓名", "效率值"))
print("-" * 66)
for i in range(n):
    print("%40s%16.0f" % (id_names[player_efficiency_list[i][0]], player_efficiency_list[i][1]))
