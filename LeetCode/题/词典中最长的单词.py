'''
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成
。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1:

输入: 
words = ["w","wo","wor","worl", "world"]
输出: "world"
解释: 
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2:

输入: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"
解释: 
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
注意:

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。
'''


def longestWord(words):
    """
    :type words: List[str]
    :rtype: str
    """
    # 耗时
    # if 1 <= len(words) <= 1000:
    #
    #     def sort_w(x):
    #         return len(x), x
    #     new_list = sorted(words, key=sort_w, reverse=True)
    #     # print(new_list)
    #     # ['banana', 'apply', 'apple', 'appl', 'app', 'ap', 'a']
    #     same_list1 = []
    #
    #     for i in new_list:
    #         result = ""
    #         if 1 <= len(i) <= 30:
    #             flag = 0
    #             for j in i:
    #                 result += j.lower()
    #                 if result not in new_list:
    #                     break
    #                 else:
    #                     flag += 1
    #             if flag == len(i):
    #                 same_list1.append(i)
    #
    #     # print(same_list1)  # ['apply', 'apple', 'appl', 'app', 'ap', 'a']
    #
    #     name = ""
    #     for r in same_list1[1:]:
    #         if len(r) == len(same_list1[0]):
    #             name = r
    #     if len(name) != 0:
    #         return name
    #     else:
    #         return same_list1[0]

    # 进一步优化
    # if 1 <= len(words) <= 1000:
    #
    #     def sort_w(x):
    #         return len(x), x
    #
    #     new_list = sorted(words, key=sort_w, reverse=True)
    #     # print(new_list)
    #     # ['banana', 'apply', 'apple', 'appl', 'app', 'ap', 'a']
    #
    #     new_list1 = new_list.copy()
    #     for i in new_list:
    #         result = ""
    #         if 1 <= len(i) <= 30:
    #             for j in i:
    #                 result += j.lower()
    #                 if result not in new_list:
    #                     new_list1.remove(i)
    #                     break
    #     print(new_list1)
    #     final_words = new_list1[0]
    #     for r in new_list1[1:]:
    #         if len(r) == len(new_list1[0]):
    #             final_words = r
    #     if len(final_words) != 0:
    #         return final_words
    #     else:
    #         return new_list[0]

    if 1 <= len(words) <= 1000:

        def sort_w(x):
            return len(x), x

        new_list = sorted(words, key=sort_w, reverse=True)

        new_list1 = new_list.copy()
        i = 0
        while i < (len(new_list)):
            result = ""
            last_word = new_list[len(new_list) - 1 - i]
            if 1 <= len(last_word) <= 30:
                for j in last_word:
                    result += j.lower()
                    if result not in new_list:
                        new_list1.remove(last_word)
                        break
                i += 1

        final_words = new_list1[0]
        for r in new_list1[1:]:
            if len(r) == len(new_list1[0]):
                final_words = r
        if len(final_words) != 0:
            return final_words
        else:
            return new_list[0]


s = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
result1 = longestWord(s)
print(result1)
