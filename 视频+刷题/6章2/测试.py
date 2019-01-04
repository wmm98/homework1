l = [['Bvril', '3 2'], ['Candy', '4 5'], ['Tim', '3 2'], ['Sufia', '4 5'], ['Lagrange', '4 5'], ['ABill', '3 2']]
def getName(x):
    return (len(x), x[0])

l1 = sorted(l, key=getName)
print(l1)