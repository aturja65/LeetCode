class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 0
        for i in range(31):
            ans = (n & 1) | ans
            ans <<= 1
            n >>= 1
        return ans | n
