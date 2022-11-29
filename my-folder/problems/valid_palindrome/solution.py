class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        s=s.lower()
        str=""
        for i in range(len(s)):
            if s[i]>='a' and s[i]<='z' or s[i]>='0' and s[i]<='9':
                str+=s[i]
        left, right = 0,len(str)-1
        while left<right:
            if str[left]!=str[right]:
                return False
            left+=1
            right-=1
        return True
        