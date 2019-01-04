i = 1
num = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        num += 1
    if num == 20:
        break  #break执行后会跳出while循环
    i += 1
