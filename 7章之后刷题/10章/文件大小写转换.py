'''【问题描述】

 

文件src.txt存储的是一篇英文文章，将其中所有大写字母转换成小写字母存入文件dest.txt。

【样例输入】

 

src.txt里面存储内容为：  This is a Book     

【样例输出】

 

生成文件dest.txt。内容为：  this is a book
'''


f1 = open("src.txt", "r")
content = f1.read().strip()
f = open("dest.txt", "w")
f.write(content.lower())
f.close()

