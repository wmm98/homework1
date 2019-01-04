str = "0101010"
num = int(str, base=2)  # 将此字符串转为2进制
print(num)  # 42

# 此后要一直将字符串转为2进制的数
import functools
int2 = functools.partial(int, base=2)
print(int2(str))  # 42