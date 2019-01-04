#例7-2-5  累加和首次大于等于1000
#编写程序，输入m，计算sum= m+(m+1)+(m+2)+…+n，当累加和sum首次大于等于1000就结束，并输出n和sum。

m = int(input("输入第一项："))
sum = 0
while sum < 1000:
    sum += m    #即sum = sum + m
    m += 1      #即m = m + 1
print("最后一项：", m)
print("累加和：", sum)