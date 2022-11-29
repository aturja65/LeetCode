class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, n =list(accumulate(nums,mul)), list(accumulate(nums[::-1],mul))[::-1],len(nums)-1
        ans = []
        ans.append(suf[1])
        for i in range(1,n):
            ans.append(pre[i-1]*suf[i+1])
        ans.append(pre[n-1])
        return ans