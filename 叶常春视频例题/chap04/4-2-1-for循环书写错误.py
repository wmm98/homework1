# 例4-2-1  for循环语句书写错误
# 错误示例1：忘记缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 错误示例2：要循环执行的语句都要缩进4个空
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")  # 换行两次。print()一次，\n一次。
# 上一行要循环执行。但是，由于没有缩进，该语句不是循环语句的组成部分，不会循环执行。

# 错误示例3：不必要的缩进
motorcycles = ['honda', 'yamaha', 'suzuki', '宗申', '钱江']
print("摩托车品牌列表的长度：", len(motorcycles))

# 错误示例4：循环语句后面的语句不要缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")
# 按作者意图，上一行不要循环执行。但是缩进使得该语句循环执行。这是逻辑错误。

# 错误示例5：遗漏冒号
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
