import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and math.log(n,4).is_integer()