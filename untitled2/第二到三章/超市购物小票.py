"""

问题描述】某超市促销，对购买的第二件商品（不限商品类别）打9折。路人甲购买两件商品，请按要求输出购物小票。
【输入形式】两个商品的原价
【输出形式】两个商品的购买价格及总价（请注意保留小数点后两位有效数字）。输出的每一行占16格。价格和总价靠右对齐。
【样例输入】

5.6  78.95
【样例输出】

            5.60

           71.06

----------------

Total:     76.66

"""

" 字符串的规格 "
price1, price2 = input().split()
price1 = float(price1)
price2 = float(price2) * 0.9
Total = price1 + price2

width = 16
content_format = '%-*s%*.2f'
price_width = 10
item_width = width-price_width

print(content_format % (item_width, "", price_width, price1))
print(content_format % (item_width, "", price_width, price2))
print("-" * width)
print(content_format % (item_width, "Total:", price_width, Total))

'''
width =35
price_width=15
item_width=width-price_width
header_format='%-*s%*s'
content_format='%-*s%*.2f'
print('='*width)
print (header_format%(item_width,'菜单',price_width,'价格')
print("-"*width)

print(content_format%(item_width,"苹果",price_width,20))

'''