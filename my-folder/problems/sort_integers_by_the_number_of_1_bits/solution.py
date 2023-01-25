class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp = []
        for num in arr:
            count = bin(num)[2:].count("1")
            temp.append([count, num])
        temp.sort()
        arr = [num for count, num in temp]
        return arr
