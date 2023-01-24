class Solution:
    def countBits(self, n: int) -> List[int]:
        ans =[]
        for i in range(n+1):
            num = bin(i)
            ans.append(num.count("1"))
        return ans