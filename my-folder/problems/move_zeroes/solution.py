class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroFound = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroFound] = nums[zeroFound], nums[i]
                zeroFound += 1

