#例10-1-7  汉字编码
#读取有汉字的文件，要使用codecs模块。
import codecs

#下面的例子中,10-1-7-names.txt文件使用的是utf-8编码。
with codecs.open('chap10-data/10-1-7-names.txt', encoding='utf-8') as namesfile:
    names = namesfile.read()

print(names)

#下面的例子中，10-1-7-txt文件格式.txt文件使用的是gbk编码。
with codecs.open('chap10-data/10-1-7-txt文件格式.txt', encoding='gbk') as txtfile:
    contents = txtfile.read()

print(contents)

#utf-8编码和gbk编码都是能对汉字进行编号，但对同一个汉字，比如‘过’，两种编码给出的编号是不同的。
#能通过软件把utf-8编码文件转换为gbk编码文件，反之也行。