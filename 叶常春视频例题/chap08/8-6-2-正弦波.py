#例8-6-2  正弦波
#注意：需要事先安装matplotlib软件包。
import math
import pylab
#初始化
y_values = []
x_values = []
num = 0.0

#生成样本点
while num < math.pi * 4:
    y_values.append(math.sin(num))
    x_values.append(num)
    num += 0.1

#绘图
pylab.plot(x_values, y_values, 'ro')
pylab.show()