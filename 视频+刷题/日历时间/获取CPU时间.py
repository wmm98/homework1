import time

start = time.clock()
for i in range(10):
    print(i)
end = time.clock()
print(end - start)  # 0.00013109535064040779