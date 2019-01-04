# @Time    : 2018/12/13 10:52
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

nba_stastics_file = open("player_regular_season.csv")
lines = nba_stastics_file.readlines()

del lines[-1]
del lines[-1]

print(lines[0], end="")
# for line in lines:
#     if "James" in line:
#         print(line, end="")
# print(lines[-1])

#统计ilkid=YoungTh01这个球员的上场时间
sum_minutes = 0
for line in lines:
    stats = line.split(',')
    if "YoungTh01" == stats[0].strip():
        print(stats)
        sum_minutes += int(stats[7])

print("YoungTh01的上场时间：", sum_minutes)


#统计各个球员的上场时间
player_minutes = {}

for line_no, line in enumerate(lines[1:]):  #[1:]是跳过标题行
    stats = line.split(',')
    ilkid = stats[0].strip()
    try:
        if ilkid not in player_minutes:
            player_minutes[ilkid] = int(stats[7])
        else:
            player_minutes[ilkid] += int(stats[7])
    except ValueError as ve:
        print("line NO: ", line_no)
        print(line)
        exit(0)

print("YoungTh01的上场时间：", player_minutes['YoungTh01'])

player_minutes_list = list(player_minutes.items())
player_minutes_list.sort(key=lambda p_m: p_m[1], reverse=True)


n = int(input("对于上场时间，你要输出前多少位？\n"))
if n <= 0:
    print("输入不合法！")
    exit(0)

id_names = {}
for line_no, line in enumerate(lines[1:]):  #[1:]是跳过标题行
    stats = line.split(',')
    ilkid = stats[0].strip()
    if ilkid not in id_names:
        id_names[ilkid] = stats[2] + " " + stats[3]

print("%40s%16s" % ("姓名", "上场时间（分钟）"))
print("-" * 66)
for i in range(n):
    print("%40s%16d" % (id_names[player_minutes_list[i][0]], player_minutes_list[i][1]))