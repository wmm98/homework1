import math
h1 = float(input())
z1 = float(input())
h2 = float(input())
z2 = float(input())
h = (h1 - h2)**2
z = (z1 - z2)**2
distance = math.sqrt(h+z)
print(distance)