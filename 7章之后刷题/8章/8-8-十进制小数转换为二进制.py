def cxs2BinaryStr(xiaoshu, bitCount=10):
    '''十进制纯小数转换为二进制小数（字符串形式,小数点后部分）'''
    if xiaoshu == 0.0:
        return "0"

    bStr = ""
    fPart = xiaoshu
    # 小数部分不为0则循环
    while fPart != 0.0 and len(bStr) < bitCount:
        # 乘2取整
        intPart = int(fPart * 2)
        bStr = bStr + str(intPart)
        # 得到小数部分
        fPart = fPart * 2 - intPart

    return bStr


def decimalInt2BinaryStr(theDecimal):
    if theDecimal == 0:
        return "0"
    # 除二取余法得到二进制数（字符串形式）
    binaryStr = ""
    while theDecimal != 0:
        # 除以2得到余数，用作高位
        binaryStr = str(theDecimal % 2) + binaryStr
        theDecimal = theDecimal // 2
    return binaryStr


def xiaoShu_10to2(f, bit_count_after_dot=10):
    '''十进制小数(只考虑正数）转换为二进制小数(小数点后bit_count_after_dot位)'''
    if f < 0:
        f = -f

    # 1. 整数部分
    intPart = int(f)
    f_binary = decimalInt2BinaryStr(intPart)

    # 2.小数部分
    xsPart = f - intPart
    f_binary += "." + cxs2BinaryStr(xsPart, bit_count_after_dot)[:]

    return f_binary


f = float(input())
print(xiaoShu_10to2(f))
