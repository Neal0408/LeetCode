version1 = "1.0.1"
version2 = "1.0.2"


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = ([*map(int, v.split('.'))] for v in (version1, version2))
        d = len(v2) - len(v1)
        v1, v2 = v1 + [0] * d, v2 + [0] * -d
        return (v1 > v2) - (v1 < v2)


if __name__ == '__main__':
    s = Solution().compareVersion(version1, version2)
    print(s)
