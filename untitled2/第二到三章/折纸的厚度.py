# 转化为米
houdu = 1 / (200 * 100)
print("n" + " " + "height")
for n in range(8, 31):
    count = n
    gaodu = houdu * 2 ** count
    print(str(count) + " " + str(gaodu) + "m")  # 这里的count和gaodu分别代表折纸次数以及相应高度的变量
