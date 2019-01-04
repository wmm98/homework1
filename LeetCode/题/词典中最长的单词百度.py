# def longestWord(words):
#     """
#     :type words: List[str]
#     :rtype: str
#     """
#     ans = ""
#     wordset = set(words)
#     # {'wo', 'worl', 'wor', 'world', 'w'}
#     print(wordset)
#     for word in words:
#         if len(word) > len(ans) or len(word) == len(ans) and word < ans:
#             if all(word[:k] in wordset for k in range(1, len(word))):
#                 ans = word
#                 print(ans)
#                 # w
#                 # wo
#                 # wor
#                 # worl
#                 # world
#                 # world
#
#     return ans
#
#
# n = ["w", "wo", "wor", "worl", "world"]
# result = longestWord(n)
# print(result)


# 2、思路：
# 排序列表，从后往前遍历排序的列表，再遍历单词的子序列在不在列表中，若全在则把该单词加进结果列表中。
# 最后找出结果列表中最长的单词，若多个单词长度一样，则选择字典序最前的。
def longestWord(words):
    """
    :type words: List[str]
    :rtype: str
    """
    res = []
    if not words:
        return ""
    else:
        newWords = sorted(words)
        # print(newWords)
        # ['a', 'ap', 'app', 'appl', 'apple', 'apply', 'banana']
        for i in range(0, len(newWords)):
            # 从后往前遍历排序的列表
            last_word = newWords[len(newWords) - 1 - i]
            while last_word in newWords:
                # 历单词的子序列在不在列表中
                last_word = last_word[:-1]

                # print(last_word)

            if not last_word:  # 等价于 if last_word == ""
                res.append(newWords[len(newWords) - 1 - i])

        print(res)  # ['apply', 'apple', 'appl', 'app', 'ap', 'a']

        result = sorted(res, key=lambda x: len(x), reverse=True)

        print(result)  # ['apply', 'apple', 'appl', 'app', 'ap', 'a']

    #     flag = 0
    #     for i in range(0, len(result)):
    #         if i == len(result) - 1 or len(result[i]) != len(result[i + 1]):
    #             flag = i
    #             break
    #         else:
    #             continue
    # return "" if not result else result[i]

    final_words = result[0]
    for r in result[1:]:
        if len(r) == len(result[0]):
            final_words = r
    if len(final_words) != 0:
        return final_words
    else:
        return result[0]


n = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
result = longestWord(n)
print(result)