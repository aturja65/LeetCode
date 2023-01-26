class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for char in s:
            ans ^= ord(char)
        for char in t:
            ans ^= ord(char)
        return chr(ans)