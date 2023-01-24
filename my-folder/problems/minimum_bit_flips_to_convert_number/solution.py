class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        mask = start ^ goal
        ans = 0
        while mask != 0:
            ans += 1
            mask = (mask & (mask - 1))
        return ans