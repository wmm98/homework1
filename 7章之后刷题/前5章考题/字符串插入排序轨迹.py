'''【问题描述】

输入N个字符串，按照字典排序规则，使用插入排序算法对字符串从大到小进行排序。按输入顺序插入有序序列，输出每次插入后的排序结果。
【输入形式】

输入在第1行中给出N和K（1<=K<N<=100），此后是N行非空字符串。
【输出形式】

输出每次插入后的排序结果，包括第1次单个字符串的插入。各个排序结果分别占一行。

【样例输入】

6
best
cat
east
a
free
day
【样例输出】

best 

cat best 

east cat best 

east cat best a 

free east cat best a 

free east day cat best a
'''

n = int(input())
result = []
new_result = []

for i in range(n):
    word = input()
    result.append(word)

    result1 = sorted(result, reverse=True)
    new_result.append(result1)
# print(new_result)
for x in new_result:
    # print(x)
    for s in x:
        print(s, end=" ")
    print()