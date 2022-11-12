class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res =[]
        while nums !=[]:
            num1 = nums.pop(nums.index(max(nums)))
            num2 = nums.pop(nums.index(min(nums)))
            res.append((num1+num2)/2)
        ans =set(res)
        return len(ans)
