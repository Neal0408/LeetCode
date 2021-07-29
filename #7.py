class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            a = str(x)
            if int(a[0] + str(int(a[:-len(a):-1]))) < -2**31:
                return 0
            else:
                return int(a[0] + str(int(a[:-len(a):-1])))
        else:
            a = str(x)
            if int(a[::-1]) > 2**31 - 1:
                return 0
            else:
                return int(a[::-1])
