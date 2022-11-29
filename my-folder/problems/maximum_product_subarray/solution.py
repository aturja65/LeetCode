class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suf = nums[:], nums[::-1]
        for i in range(1,len(nums)):
            pre[i]*=pre[i-1] or 1
            suf[i]*=suf[i-1] or 1
        return max(pre+suf)