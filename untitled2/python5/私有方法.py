class Message:

    # 在方法名前加__表示私有方法，在外部不可调用
    def __test(self):
        print("正在发送短信")

    def send_massage(self, money):
        if money > 0 and money < 10000:
            self.__test()
        else:
            print("你的余额不足")




information = Message()
information.send_massage(100)