#例2-3-6  字符串拼接
first_name = "ada"
last_name = "lovelace"
# 左串 + 右串：左串尾部追加右串，组成新的字符串
full_name = first_name + " " + last_name  #拼接了两次
print(full_name)

# 拼接操作（+）本质上是一个方法。
print("Hello, " + full_name.title() + "!")

# 拼接操作（+）这个方法返回拼接得到的字符串。
message = "Hello, " + full_name.title() + "!"
print(message)