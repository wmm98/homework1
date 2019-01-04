# @Time    : 2018/12/13 10:03
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

#player_regular_season.csv中第20314行和20918行需要人工修正。做法是：
#  把第5列的"Jr."删掉。右侧的数据各自向左移动一格。
nba_stastics_file = open("player_regular_season.csv")
lines = nba_stastics_file.readlines()  #读取整个文件的每一行.lines是一份列表
# print(lines[1])

print(lines[0], end="")
for line in lines:
    if "James" in line:
        print(line, end="")

print("last 2 lines:")
print(lines[-2], end="")
print(lines[-1], end="")

nba_stastics_file.close()

#观察数据，可以得出：
#1. 第1个字段ilkid，是球员编号。
#2. 一行是一个球员一个赛季的数据。
