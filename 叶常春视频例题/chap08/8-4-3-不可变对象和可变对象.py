# 例8-4-3  不可变对象和可变对象
# 整数、浮点数对象是不可变的。修改它实质上是新建了一个对象。
x = 2.0
print("1. id(x)=", id(x))
x = x * x  # 生成一个新对象存储4.0这个值
print("2. id(x)=", id(x))

# 字符串是不可变的。
s = "hello"
print("3. id(s)=", id(s))
s = s.title()  # 生成了一个新字符串对象存储"Hello, Everyone."
print("4. id(s)=", id(s))

# 列表，字典是可变的。它们的内容可以变化。
name_list = ['li', 'zhang', 'guo']
print("5. namelist=", name_list)
print("5. id(namelist)=", id(name_list))
name_list[0] = 'xie'
print("6. namelist=", name_list)
print("6. id(namelist)=", id(name_list))

# 字典是可变的
word_dict = {'object': '对象', 'class': '类'}
print("7. word_dict=", word_dict)
print("7. id(word_dict)=", id(word_dict))
word_dict['object'] = '物体'
print("8. word_dict=", word_dict)
print("8. id(word_dict)=", id(word_dict))
