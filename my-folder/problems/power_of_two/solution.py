import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n%2!=0 or n==0:
            return False    
        res = math.floor(math.log2(abs(n)))
        if 2**res == n:
            return True
        else:
            return False