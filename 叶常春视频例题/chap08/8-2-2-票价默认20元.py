#例8-2-2  票价默认20元
#程序功能：合计电影票的价格。单张电影票的价格一般是20元，热门大片可能卖到30元。
#   6岁（含）以下的儿童，免票。6岁到14岁，半价。65岁以上也是半价。

#函数get_price计算实际的单张电影票价。
#  参数price用于传递基准价。默认值是20元。
#  参数age_type用于区分观众的年龄分段。1: <=6. 2: 6~14. 3: 14~65. 4: >65.
#  age_type的默认值是3.
def get_price(price=20, age_type = 3):
    if age_type == 1:
        return 0
    elif age_type == 2:
        return price * 0.5
    elif age_type == 3:
        return price
    elif age_type == 4:
        return price * 0.5

print("一名5岁儿童，2张基准价票（20元），一名65岁以上老人的合计票价：")
total = get_price(age_type=1) + get_price()*2 + get_price(age_type=4)
print(total)