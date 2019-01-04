#例7-2-4  反复输入
#反复输入，直至遇到quit。
#例7-2-2是第一个版本。这是第二个版本。
while True:
    astr = input("-->")
    if astr == "quit":
        break

    print(astr)
print("bye.")