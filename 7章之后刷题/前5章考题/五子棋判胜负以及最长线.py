'''【问题描述】

已知两人分别执白棋和黑棋在一个围棋棋盘上下五子棋，若同一颜色的棋子在同一条横行、纵行或斜线上连成5个棋子，则执该颜色棋子的人获胜。
编写程序读入某一时刻下棋的状态，并判断是否有人获胜。
输入的棋盘大小是19×19，用数字0表示空位置（即没有棋子），用数字1表示该位置下了一白色棋子，用数字2表示该位置下了一黑色棋子。
假设同一颜色的棋子在同一条横行、纵行或斜线上连成的棋子个数不会超过5个，并且最多有一人连成线的棋子个数为5。

【输入形式】

从控制台输入用来表示棋盘状态的数字0、1或2；每行输入19个数字，各数字之间以一个空格分隔，每行最后一个数字后没有空格；
共输入19行表示棋盘状态的数字。

【输出形式】

若有人获胜，则先输出获胜人的棋子颜色（1表示白色棋子，2表示黑色棋子），然后输出英文冒号:，最后输出连成5个棋子连线的起始位置
（棋盘横行自上往下、
纵行自左往右从1开始计数，横行最小的棋子在棋盘上的横行数和纵行数作为连线的起始位置，两数字之间以一个英文逗号,作为分隔符）。
若没有人获胜，则输出当前同一颜色的棋子在同一条横行、纵行或斜线上连成最长线的棋子个数。

【输入样例1】

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 2 0 1 1 2 0 0 0 0 0 0 0
0 0 0 0 0 2 1 1 1 1 2 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 2 1 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 2 2 0 0 0 0 0 0 0 0
0 0 0 0 0 2 0 1 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 1 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

【输出样例1】

1:9,8

【输入样例2】

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

【输出样例2】

2


【样例说明】

在输入的样例1中，执白棋（数字1表示）的人已经获胜，连成5个棋子的起始位置在第9行第8列，所以输出1:9,8。
在输入的样例2中，还没有同一颜色的棋子连成5个，所以无人获胜；连成最长线的棋子个数为2，所以输出2。'''