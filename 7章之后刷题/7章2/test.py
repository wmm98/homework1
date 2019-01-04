def zhi_shu(m):
    # 素数大于1
    if m > 1:
        for r in range(2, m):
            if m % r == 0:
                return False
        else:
            return True
    # 小于等于1的不是素数
    else:
        return False
