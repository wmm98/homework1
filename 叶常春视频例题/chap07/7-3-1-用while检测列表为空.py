#例7-3-1  用while语句检测列表是否为空
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:  #当unconfirmed_users列表不为空，则...
    current_user = unconfirmed_users.pop()
    print("正在验证用户: " + current_user.title())  #模仿验证用户动作
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\n以下用户验证通过:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())