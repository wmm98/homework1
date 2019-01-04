#例8-1-3  公因子
#求x, y的公因子
def gyz(x, y):
    yz = x
    while yz > 0:
        if x % yz == 0 and y % yz == 0:
            return yz
        else:
            yz -= 1

print("35和21的公因子是：", gyz(35, 21))
print("24和18的公因子是：", gyz(24, 18))