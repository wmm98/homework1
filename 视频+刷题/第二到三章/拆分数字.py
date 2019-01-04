num = int(input())
ab = num // 100
cd = num % 100
if num == (ab+cd)*(ab+cd):
    print("1")
else:
    print("0")



