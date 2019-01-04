#例8-1-1  定义函数
#定义函数
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
    print("Nice to meet you.")

#调用函数
greet_user('库里')

#三重引号括起来的文字，即显示简单的问候语，是注释。