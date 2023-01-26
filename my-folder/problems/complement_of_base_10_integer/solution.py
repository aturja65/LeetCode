class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask, temp = 0, n
        while temp:
            mask = (mask << 1) | 1
            temp >>= 1
        return mask ^ n