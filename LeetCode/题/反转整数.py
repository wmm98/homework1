'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x > 0:
        s = str(x).strip("0")
        s1 = s[::-1]
        if int(s1) <= 2 ** 31 - 1:
            return s1
        else:
            return 0
    elif x == 0:
        return 0
    else:
        s = str(x).strip("0")
        s11 = s[::-1]
        s1 = s11[:-1]
        if -2 ** 31 <= -int(s1):
            return -int(s1)
        else:
            return 0

n = int(input())
n1 = reverse(n)
print(n1)

