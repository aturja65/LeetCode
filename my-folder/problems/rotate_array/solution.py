class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if k<=len(nums):
        k%=len(nums)
        index = len(nums)-k
        temp =[]
        for i in range(index,len(nums)):
            temp.append(nums[i])
        for i in range(index):
           temp.append(nums[i])
        for i in range(len(nums)):
            nums[i]=temp[i]