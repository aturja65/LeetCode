class Solution:
    def binaryGap(self, n: int) -> int:
        ans, count = 0, 0
        while n:
            if n & 1:
                if count != 0:
                    ans = max(ans, count)
                    count = 1
                else:
                    count += 1
            elif count != 0:
                count += 1
            n >>= 1
        return ans