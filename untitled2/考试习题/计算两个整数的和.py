'''【问题描述】计算两个整数的和
【输入形式】两个整数
【输出形式】上述两个整数的和
【样例输入】1 2
【样例输出】3
【样例说明】输入的1和2是两个整数，程序将自动计算1和2的和，也就是3，并且将3输出。
【评分标准】根据不同的输入，输出正确的数，即可得分'''

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)