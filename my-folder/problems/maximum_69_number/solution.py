class Solution:
    def maximum69Number (self, num: int) -> int:
        l = list(str(num))
        for i, value in enumerate(l):
            if value == '6':
                l[i]='9'
                break
        return int("".join(l))