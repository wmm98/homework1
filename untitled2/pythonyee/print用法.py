wws = int(input())
w1 = wws // 10000
w2 = (wws - w1 * 10000) // 1000
w3 = (wws - w1 * 10000 - w2 * 1000) // 100
w4 = (wws - w1 * 10000 - w2 * 1000 - w3 * 100) // 10
w5 = wws % 10
print(w1, " ", w2, " ", w3, " ", w4, " ", w5)


