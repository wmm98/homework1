'''
给定一个字符串 s，找到 s 子中最长的回文串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

def longestPalindrome(s):

    if len(s) > 0:
        flag = 0
        max_string = ''
        for i in range(len(s)):
            list1 = s[i]
            for j in range(i + 1, len(s)):
                list1 += s[j]
                if list1 == list1[::-1]:
                    flag += 1
                    if len(max_string) < len(list1):
                        max_string = list1
            if len(max_string) == len(s) - i:
                return max_string

        if flag == 0:
            return s[0]

        return max_string
    else:
        return ""


s = input()
s1 = longestPalindrome(s)
print(s1)