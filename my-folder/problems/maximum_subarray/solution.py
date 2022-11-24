class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum =0
        mx_sum = nums[0]
        if len(nums)==1:
            return nums[0]
        for i in nums:
            cur_sum+=i
            mx_sum = max(mx_sum,cur_sum)
            if cur_sum<0:
                cur_sum=0
        return mx_sum