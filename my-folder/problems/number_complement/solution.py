class Solution:
    def findComplement(self, num: int) -> int:
        mask, temp = 0, num
        while temp:
            mask = (mask<<1) | 1
            temp >>= 1
        return mask ^ num