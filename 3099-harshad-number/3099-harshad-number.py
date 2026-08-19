class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        k=x
        res=0
        while x>0:
            d=x%10
            res+=d
            x//=10
        ans=k%res
        if ans==0:
            return res
        return -1
        