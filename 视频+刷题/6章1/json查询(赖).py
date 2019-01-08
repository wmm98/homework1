
import json
json_text = ""
n, m = input().split()
n = int(n)
m = int(m)
while n > 0:
    temp = input()
    json_text += temp
    n -= 1
json_dict = json.loads(json_text)
tempList = []
while m > 0:
    tempList.append(input())
    m -= 1
for i in tempList:
    if i in json_dict:
        print(json_dict[i])
    else:
        print("NOTEXIST")