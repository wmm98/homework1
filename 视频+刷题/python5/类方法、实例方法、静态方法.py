class Tool(object):
    # 类对象
    num = 0

    # 实例方法
    def __init__(self):
        # 实例对象
        self.name = "小吴"

    #  类方法
    @classmethod
    def tool(cls):
        cls.num = 100

    # 静态方法
    @staticmethod
    def tool1():
        print("----静态方法----")


t = Tool()
# Tool.tool()  # 可以通过类的名字来调用类方法
t.tool()  # 也可以通过创建一个对象来调用类方法
print(Tool.num)

# 调用静态方法
Tool.tool1()
# t.tool1()
