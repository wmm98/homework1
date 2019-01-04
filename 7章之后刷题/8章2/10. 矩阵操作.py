def read_matrix(n):
    '''从标准输入读入n*n的整数矩阵'''
    m = []
    for r in range(n):
        row = [int(x) for x in input().split()]
        m.append(row)
    return m

def find_min(matrix):
    '''在矩阵matrix中找到最小值'''
    min_value = matrix[0][0]
    for row in matrix:
        for column in row:
            if column < min_value:
                min_value = column
    return min_value

def find_max(matrix):
    '''在矩阵matrix中找到最大值'''
    max_value = max(matrix[0])
    for i in range(1, len(matrix)):
        row_max = max(matrix[i])
        if max_value < row_max:
            max_value = row_max
    return max_value

def sum_matrix(matrix):
    '''求矩阵各元素的和'''
    sum_value = 0
    for row in matrix:
        sum_value += sum(row)
    return sum_value

n = int(input())
matrix = read_matrix(n)
max_value = find_max(matrix)
min_value = find_min(matrix)
sum_value = sum_matrix(matrix)

for r in range(1, n - 1):
    for c in range(1, n - 1):
        matrix[r][c] = sum_value

matrix[n // 2][n // 2] = max_value

for c in range(n):
    matrix[0][c] = min_value
    matrix[n - 1][c] = min_value

for r in range(n):
    matrix[r][0] = min_value
    matrix[r][n - 1] = min_value

for row in matrix:
    for column in row:
        print("%5d" % column, end='')
    print('')
