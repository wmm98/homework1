def read_matrix(n):
    '''读入n行n列,生成n*n矩阵'''
    mtx = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        mtx.append(row)
    return mtx

def add(left, right):
    '''两个矩阵相加，返回结果'''
    n = len(left)
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(left[r][c] + right[r][c])
        result.append(row)
    return result

def minus(left, right):
    '''返回矩阵left-right的结果'''
    n = len(left)
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(left[r][c] - right[r][c])
        result.append(row)

    return result



n = int(input())
left = read_matrix(n)
operator = input().strip()
while operator != '#':
    right = read_matrix(n)
    if operator == '+':
        left = add(left, right)
    elif operator == '-':
        left = minus(left, right)
    operator = input().strip()

for r in range(n):
    for c in range(n):
        print("%5d" % left[r][c], end='')
    print('')
