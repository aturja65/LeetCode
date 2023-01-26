class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        while l<len(nums)-1:
            if nums[l] == nums[r]:
                ans += 1
            if r == len(nums)-1:
                l += 1
                r = l+1
            else:
                r += 1
        return ans