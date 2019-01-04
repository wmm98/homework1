#例7-3-3  继续回答吗
#反复输入，直至用户回答不再继续
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n你的姓名? ")
    response = input("将来你想攀登哪座山? ")
    # 将答卷存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("还有人愿意参加调查吗? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- 调查结果 ---")
for name, response in responses.items():
    print(name + " 想攀登 " + response + ".")