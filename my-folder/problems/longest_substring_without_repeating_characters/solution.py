class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str=""
        ans=0
        for value in s:
            while value in str:
                str=str[1:]
            str+=value
            ans=max(ans,len(str))
        return ans