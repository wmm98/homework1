# 例4-3-1  range函数生成数字列表
# range(1, 5)生成[1, 2, 3, 4]
for value in range(1, 5):
    print(value)

# 在C++，实现上述语句的功能的写法大致是：
#    for (int i = 1; i < 5; i++)
#        cout << i << endl;
# 在Java中，实现上述语句的功能的写法大致是：
#    for (int i = 1; i < 5; i++)
#        System.out.print( i );

print("要生成1-5的列表，用range(1, 6).")
# 要生成1-5的列表，用range(1, 6)
for value in range(1, 6):
    print(value)

# range()函数生成一个对象。该对象含有数字列表。
numbers = range(1, 6)
print("numbers:", numbers)
print("type(numbers):", type(numbers))  # type函数返回值的类型
print("numbers内的列表：", list(numbers))  # list函数返回range对象包含的数字列表。

# range(2,11,2)参数说明：
# 第一个参数指定数字列表的第一项是多少。这里为2.
# 第二个参数指定数字列表的上/下界（不含）是多少。这里为11.
# 第三个参数指定数字列表的相邻项之间的增量是多少。这里为2.
even_numbers = list(range(2, 11, 2))  # 先执行range(),而后执行list()
print("even_numbers:", even_numbers)

# 数字列表元素值的平方组成的列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)  # append方法项列表尾部添加元素
print("squares:", squares)

# 只有1个参数的情形。这个参数用作上/下界。
print("list(range(9)):", list(range(9)))  # range(9)的列表第一项是0.
# 递减的数字列表
print("list(range(9, 1, -1))", list(range(9, 1, -1)))  # 增量为-1，即递减

# 对数字列表进行统计
numbers = list(range(10))
print("sum(numbers):", sum(numbers))
print("max(numbers):", max(numbers))
print("min(numbers):", min(numbers))
