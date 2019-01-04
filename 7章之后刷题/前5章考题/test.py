def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result1 = ""
    for i in l1:
        result1 = str(i) + result1

    result2 = ""
    for j in l2:
        result2 = str(j) + result2

    result = (int(result1) + int(result2))
    new_list = []
    for r in str(result):
        new_list.append(int(r))
    return new_list

a = [2, 4, 3]
b = [5, 6, 4]
result3 = addTwoNumbers(a, b)
print(result3)

