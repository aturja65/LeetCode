class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num!= 0:
            if num&1 == 0:
                num>>=1
            else:
                num-=1
            ans+=1
        return ans