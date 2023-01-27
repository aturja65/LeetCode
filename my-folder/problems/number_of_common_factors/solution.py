class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        minVal = min(a,b)
        maxVal = max(a,b)
        ans, i = 0, 1
        while i*i <= minVal:
            if minVal%i==0 and maxVal%i==0:
                ans += 1
            div = minVal//i
            if minVal%i==0 and maxVal%div==0 and i != div:
                ans += 1
            i += 1
        return ans