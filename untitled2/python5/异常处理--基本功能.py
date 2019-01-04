# coding = utf-8

try:
    f = open("xxxx.txt")
    d = 3 / 0
    print(num)
    print("你好")

except(FileNotFoundError, ZeroDivisionError):
    print("捕获到异常，进行处理")


# except Exception:
# print("除了以上的异常之外的异常")

except Exception as ret:  # 能知道除了以上异常以为错误原因 ret为随意的变量名
    print(ret)


else:
    print("没有异常后执行的功能")

finally:
    print("有没有异常都执行的人功能")

print("----2----")
