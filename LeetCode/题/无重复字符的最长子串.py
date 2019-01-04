'''给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。'''


# def lengthOfLongestSubstring(s):
#     if len(s) != 0:
#         result_list = []
#         for i in range(len(s)):
#             list1 = [s[i]]
#             for j in range(i + 1, len(s)):
#                 if s[j] not in list1:
#                     list1.append(s[j])
#                     result_list.append(list1)
#                 else:
#                     break
#         length = 0
#         for r in result_list:
#             if len(r) >= length:
#                 length = len(r)
#         if length == 0:
#             return 1
#         else:
#
#             return length
#     else:
#         return 0

# 当数据量大的时候，用列表来存储数据往往会出现运行时间过长的问题，最好不要盲目用列表
def lengthOfLongestSubstring(s):
    if len(s) != 0:
        result_list = []
        for i in range(len(s)):
            y = s[i]
            result = y
            for j in range(i + 1, len(s)):

                if s[j] in result:
                    break
                else:
                    result += s[j]
            result_list.append(result)

        length = 0
        for r in result_list:
            if len(r) >= length:
                length = len(r)
        if length == 0:
            return 1
        else:

            return length
    else:
        return 0

a = input()
s = lengthOfLongestSubstring(a)
print(s)






