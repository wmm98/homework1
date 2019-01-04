#例7-2-2  反复输入
#反复输入，直至遇到quit
astr = input("-->")
while astr != "quit":
    print(astr)
    astr = input("-->")
print("bye.")