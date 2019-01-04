big_n = input().strip()
del_num = int(input())

for i in range(del_num):
    for j in range(len(big_n)):
        if j < len(big_n) - 1 and big_n[j] > big_n[j + 1]:
            big_n = big_n[:j] + big_n[j + 1:]
            break
        elif j == len(big_n) - 1:
            big_n = big_n[:j]

print(big_n)