#例2-4-2  浮点数
print("0.1 + 0.1 = ", 0.1 + 0.1)
print("0.1 - 0.1 = ", 0.1 - 0.1)
print("0.1 * 0.1 = ", 0.1 * 0.1)  #计算机无法精确存储0.01，存储了它的近似值。
print("0.1 / 0.1 = ", 0.1 / 0.1)

a = 0.2
b = 0.1
print("a + b = ", a + b)  #计算机无法精确存储0.3，存储了它的近似值。

#对大多数浮点数，计算机都无法精确存储。这造成误差。
#在用计算机解决现实问题时，要考虑上述误差的积累。