l = [['1', 'aaa', '21'], ['45', 'bbbb', '20'], ['110', 'eee', '20'], ['54', 'ddd', '20']]


def getKeyName(x):
    return len(x[1])

message = sorted(l, key=getKeyName)
print(message)

# def getKeyAge(x):
#     return x[2]
#
# message1 = sorted(message, key=getKeyAge)

# print(message1)

# [['1', 'aaa', '21'], ['45', 'bbb', '20'], ['54', 'ddd', '20'], ['110', 'eee', '20']]
# [['45', 'bbb', '20'], ['54', 'ddd', '20'], ['110', 'eee', '20'], ['1', 'aaa', '21']]