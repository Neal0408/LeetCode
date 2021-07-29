from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution().longestCommonPrefix(strs)
    print(s)