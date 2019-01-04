#例7-2-6  整数尾部有几个0

n = int(input("输入整数："))

cnt = 0
while n % 10 == 0:
    n = n / 10
    cnt += 1
print("尾部有" + str(cnt) + "个0.")