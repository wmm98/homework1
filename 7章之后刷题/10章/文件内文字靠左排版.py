'''英文电影中参演人员名单一般以某种方式进行排版显示。给定一个未排版的文件listin.txt，
该文件中每行参演人员名单由冒号':'分隔成前后两部分，但格式杂乱无章，单词（由除空格和水平制表符之外的其它字符构成）
之间可能有多个空格或水平制表符分隔。编写程序，要求将其按如下排版规则排版输出到另一个文件listout.txt中：

1.从标准输入（即键盘）读取一整数，作为排版后所有各行冒号':'在一行中的固定位置；假设输入的整数肯定大于排版后所有
各行冒号':'前的字符个数，位置从1开始计数；

2.冒号':'左边的单词串以行头为基准左对齐，左边的最后一个单词与冒号之间以空格填充；
冒号':'右边的单词串以冒号':'为基准左对齐，最后一个单词后只有回车换行符，不再有其它字符；

3.冒号':'左右两边的单词间都只有一个空格分隔，并且要求冒号两边至少各有一个空格。

假设输入文件中每行字符个数不超过100。

【输入形式】

待排版的参演人员名单从当前目录下的listin.txt文件中读入；表示冒号':'位置的整数从标准输入读入。

【输出形式】

排版后的参演人员名单输出到当前目录下的listout.txt中。

【输入样例】

假设文件listin.txt内容为：

   Digital Intermediate by :   EFILM 

Supervising    Digital Colorist : STEVEN J. SCOTT  

 Second Colorist :ANDREW FRANCIS

 Digital Intermediate Producer:LOAN PHAN

Digital  Intermediate Editor:  DEVON MILLER     

表示冒号固定位置的整数为：
40
【输出样例】
文件listout.txt中的内容应为：

【样例说明】
输入的文件listin.txt中有五行参演人员名单，
要求排版后冒号':'位于第40个字符的位置，按照上述排版规则输出到文件listout.txt中。
【评分标准】
该题要求按照排版规则对文件内容进行排版。'''

n = int(input())
f = open("listin.txt")

f1 = open("listout.txt", "w+")
content = f.readlines()
for line in content:
    result = ""
    line = line.strip().split(":")
    # print([i for i in line[0].split(" ") if i != ""])
    for j in [i for i in line[0].split() if i != ""]:
        result += j + " "
    result = result.strip()
    print(result)

    result1 = ""
    for s in [r for r in line[1].split() if r != ""]:
        result1 += s + " "
    result1 = result1.strip()

    f1.write(result.rjust((n - 1), " ") + ":" + " " + result1 + "\n")

f.close()
f1.close()

