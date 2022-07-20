class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(nums==[]):
            return [-1,-1]
        low=-1
        up=len(nums)
        while(low+1<up):
            i=(low+up)//2
            if(nums[i]<=target):
                low=i
            else:
                up=i
        if(nums[low]!=target):
            return [-1,-1]
        j=low
        low=-1
        up=len(nums)
        while(low+1<up):
            i=(low+up)//2
            if(target<=nums[i]):
                up=i
            else:
                low=i
        return [up,j]