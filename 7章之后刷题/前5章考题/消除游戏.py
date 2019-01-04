'''
消除类游戏是深受大众欢迎的一种游戏，游戏在一个包含有n行m列的游戏棋盘上进行，棋盘的每一行每一列的方格上放着一个有颜色的棋子，
当一行或一列上有连续三个或更多的相同颜色的棋子时，这些棋子都被消除。当有多处可以被消除时，这些地方的棋子将同时被消除。

现在给定一个n行m列的棋盘，棋盘中的每一个方格上有一个棋子（用数字1-9表示各种颜色的棋子），请给出经过消除后的棋盘。

请注意：一个棋子可能在某一行和某一列同时被消除。

【输入形式】

从标准输入读取数据，第一行包含两个整数n和m，分别表示棋盘的行数和列数（行数和列数都大于等于3，小于等于9），以一个空格分隔这两个整数。

接下来输入n行，每行m个整数，用一个空格分隔各个整数，这些整数分别表示每一个方格中棋子的颜色（大于等于1，小于等于9）。

【输出形式】

向标准输出上输出n行，每行m个整数，相邻整数之间以一个空格分隔，表示经过消除后的棋盘。如果一个方格中的棋子被消除，
则对应的方格输出数字0，否则输出代表原棋子颜色的整数。每行最后一个整数后也要有一个空格。

【样例1输入】

4 5

2 2 3 1 2

3 4 5 1 4

2 3 2 1 3

2 2 2 4 4

【样例1输出】

2 2 3 0 2 

3 4 5 0 4 

2 3 2 0 3 

0 0 0 4 4 

【样例1说明】

棋盘中第4列的1和第4行的2可以被消除，其它方格中的棋子均被保留。

【样例2输入】

4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3

【样例2输出】

2 2 3 0 2 

3 0 0 0 0 

2 3 2 0 3 

2 2 0 0 0 

【样例2说明】

棋盘中第4列的1，第二行的1和第4行的3可以被消除，其它方格中的棋子均被保留。'''

n, m = input().split()
n = int(n)
m = int(m)
game = []
if 3 <= n <= 9 and 3 <= m <= 9:
    for i in range(n):
        lie = [int(j) for j in input().split()]
        game.append(lie)

# 设定一个全为0的矩阵
game1 = []
for i1 in range(n):
    lie1 = [0 for i in range(m)]
    game1.append(lie1)


for s in range(n):
    shu = game[s][0]
    for l in range(1, m):
        # if shu == game[s][l] and shu == game[s][l + 1]:
        #     shu = game[s][l + 2]
        #     continue
        # elif shu == game[s][l] and shu != game[s][l + 1]:
        #     shu = game[s][l + 1]
        #     game1[s][l] = game[s][l]
        #     game1[s][l - 1] = game[s][l - 1]
        # elif shu != game[s][l]:
        #     shu = game[s][l]
        #     game1[s][l] = game[s][l]

        if shu == game[s][l]:
            if shu == game[s][l + 1]:
                continue
            else:
                game1[s][l] = game[s][l]
                game1[s][l - 1] = game[s][l - 1]
                shu = game[s][l]
        else:
            game1[s][l] = game[s][l]
            shu = game[s][l]

print(game1)




