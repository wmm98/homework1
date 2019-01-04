def sum_random(a, b, *args):  # *变量名表示后面可以有多个参数，调用时输出为元祖的形式
    print(a)
    print(b)
    print(args)
    result = a + b
    for sum in args:
        result+=sum
    print(result)


sum_random(1, 2, 2, 3, 3)  # 输出为1,2，（2,3,3）
# sum_random(1, 1, 1)#输出为1,1，（1，）元祖只有一个元素的时候的表达式
# sum_random(1, 1)#输出为1,1，（）

'''当为不确定多少个参数的时候用此方法'''
