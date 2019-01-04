#例5-1-2  汽车品牌名的大小写
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':        #if语句隶属于for语句的语句块
        print(car.upper())  #结论为真情形的语句块
    else:
        print(car.title())  #条件为加情形的语句块

#upper()方法是把全部字母变成大写。
#title()方法是把首字母变成大写。