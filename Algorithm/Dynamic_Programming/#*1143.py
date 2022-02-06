# 1143.最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 解题思路
# 1.对这题也只有个是个动态规划的题的印象，剩下就连怎么切入都觉得有点生疏。还是要多刷点题。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


obj = Solution()
