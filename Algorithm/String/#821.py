# 821.字符的最短距离
# 给你一个字符串 s 和一个字符c，且 c 是 s 是中出现过的字符。
# 解题思路
# 1.做两遍遍历分别从左到右和从右到左，prev 记录最近一次 c 出现的位置，而每个位置都跟最近的
# c做差值则是当前离最近的 c 的距离。
from typing import List


class Solution:

    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, x in enumerate(s):
            if x == c:
                prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


obj = Solution()
