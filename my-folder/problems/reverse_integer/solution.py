class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            num=-x
            ans=0
            while num>0:
                rem=num%10
                ans=(ans*10)+rem
                num=floor(num/10)
            if -ans<-2147483648:
                return 0
            return -ans
        else:
            num=x
            ans=0
            while num>0:
                rem=num%10
                ans=(ans*10)+rem
                num=floor(num/10)
            if ans>2147483647:
                return 0
            return ans