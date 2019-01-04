# 就是转换字符串的时候，并不会改变原来的字符串，只是返回了一个修改的值
# uiou&hjhkj-ioio 表示的是三个字符
str = "uiouioo uiou&hjhkj-ioio"
print(str.title())  #   结果 Uiouioo Uiou&Hjhkj-Ioio
print(str)  # 输出结果 uiouioo uiou&hjhkj-ioio

# 注意点：\n 整体是代表一个字符，\代表一个字符