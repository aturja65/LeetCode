class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = x ^ y
        ans = 0
        while mask != 0:
            ans+=1
            mask = mask & (mask-1)
        return ans