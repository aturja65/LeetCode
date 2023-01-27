class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return sum(arr)
        ans = 0
        comb = [[]]
        for value in arr:
            comb.append([value])
        for i in range(3, len(arr)+1, 2):
            l, r = 0, i        
            while r <= len(arr):
                comb.append(arr[l:r])
                l += 1
                r += 1
        for value in comb:
            ans += sum(value)
        return ans