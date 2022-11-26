from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i], nums[j] =nums[j], nums[i]
        self.revlist(nums,i+1)
    
    def revlist(self,nums,start):
        end = len(nums)-1
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1