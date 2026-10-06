class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        res=0
        while l<=h:
            mid=(l+h)//2
            if mid*mid<=x:
                res=mid
                l=mid+1
            else:
                h=mid-1
        return res
        