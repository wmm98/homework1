# 填充 字符串左移
name = "wumingming"
print(name.ljust(16, "*"))  # 表示长度为16，填充了16-len(name)个*
#  wumingming******

# 填充 字符串右移
name = "wumingming"
print(name.rjust(16, "*"))  # 表示长度为16，填充了16-len(name)个*
# ******wumingming

# 填充 字符串向中间靠拢
name = "wumingming"
print(name.center(19, "*"))  # 表示长度为16，填充了16-len(name)个*,要是不够分，左边就会多一个*
# *****wumingming****

# 其中填充的字符长度只能为1

# 压缩
word = " nihao clsdjckl uods lcjkl0 0000*"
# 从做搜索
print(word.lstrip())  # 左边的空格没有了
print(word.rstrip("*"))  # 左边的空格没有了
# nihao clsdjckl uods lcjkl0 0000
print(word.strip())   # 左右的空格都没有了

word1 = "nihohio dljdslk oooo"
print(word1.lstrip("ni"))  # 左边的ni没有了
print(word1.rstrip("o"))  # 右边的o没有了

