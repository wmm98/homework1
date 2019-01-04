'''【输入格式】

输入有两行。

第一行表示实数数组的元素个数N（N < 1000）;

第二行表示输入的实数数组，包含N个元素，元素之间用空格分隔。

 

【输出格式】

输出只有一行，即输入数组的标准方差；保留3位小数。

 

【样例输入】

4
23.45 35.7 54.89 47

 

【样例输出】

11.225

 
 	'''
import math

def std(n, num):
    avg = sum(num) / n
    cha_he = 0
    for i in num:
        cha_he += (i - avg) ** 2
    result = math.sqrt(cha_he / n)
    return "%0.3f" % result

n = int(input())
num = [float(i) for i in input().split()]
one = std(n, num)
print(one)