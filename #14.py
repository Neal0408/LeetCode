# 14.最长公共前缀
# 编写一个函数来查找字符串数组中最长的公共前缀。
# 解题思路
# 1.Python 特性，取每个单词的同一位置的字母查看是否相同。
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            print(tmp_set)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


obj = Solution()
