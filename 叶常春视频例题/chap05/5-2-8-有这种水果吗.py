#例5-2-8
fruits = ['红富士', '龙眼', '荔枝', '贡梨', '黄元帅', '布林', '水蜜桃']
query = input("输入要查询的水果：")
if query in fruits:
    print("有货")
else:
    print("没货")