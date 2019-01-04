#例8-4-2  传递列表

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['zhang', 'li', 'wang']
greet_users(usernames)  #names参数复制了usernames的引用
