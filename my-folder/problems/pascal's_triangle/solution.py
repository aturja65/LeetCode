class Solution:
    def fact(self, n):
        if n == 0:
            return 1
        return n * self.fact(n-1)
    def combination(self, n, r):
        return self.fact(n)//(self.fact(n-r)*self.fact(r))
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([self.combination(i,j)for j in range(i+1)])
        return ans