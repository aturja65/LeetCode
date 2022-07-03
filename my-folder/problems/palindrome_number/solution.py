class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=f"{x}"
        b="".join(reversed(a))
        return a==b