
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        dup = [x for x in nums if x in visited or (visited.add(x) or False)]
 
        return dup[0]
        