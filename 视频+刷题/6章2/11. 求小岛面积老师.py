n = int(input())
sea = []
for r in range(n):
    sea.append(input().split())
# print(sea)

#求出各行的最左边1和最右边1的坐标
row_left_right = []
for r in range(n):
    left_right = [None, None]
    for c in range(n):
        if sea[r][c] == '1':
            if left_right[0] == None:
                left_right[0] = c
            if left_right[1] == None or left_right[1] < c:
                left_right[1] = c
    row_left_right.append(left_right)
# print(row_left_right)
#求出各列的最上方1和最下端1的坐标
column_upper_lower = []
for c in range(n):
    upper_lower = [None, None]
    for r in range(n):
        if sea[r][c] == '1':
            if upper_lower[0] == None:
                upper_lower[0] = r
            if upper_lower[1] == None or upper_lower[1] < r:
                upper_lower[1] = r
    column_upper_lower.append(upper_lower)
# print(column_upper_lower)

def is_land(row, column, row_left_right, column_upper_lower):
    if row_left_right[row][0] == None:
        return False
    if column_upper_lower[column][0] == None:
        return False
    if row_left_right[row][0] < column < row_left_right[row][1] and \
        column_upper_lower[column][0] < row < column_upper_lower[column][1]:
        return True
    else:
        return False

land_area = 0
for r in range(n):
    for c in range(n):
        if sea[r][c] == '0':
            in_land_area = is_land(r, c, row_left_right, column_upper_lower)
            # print(r, c, ":", in_land_area)
            if in_land_area:
                land_area += 1

print(land_area)