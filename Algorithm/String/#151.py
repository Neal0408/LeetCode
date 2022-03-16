# 151.翻转字符串里的单词
# 给你一个字符串s，逐个翻转字符串中的所有单词。
# 解题思路
# 1.第一种方法是直接使用Python API，来完成这个事情。首先是split，然后反转reversed，最后是
# 字符串join。
# 2.第二种是使用双端队列可以前后插入的特性。
import collections


class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        d = collections.deque()
        word = []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


obj = Solution()
