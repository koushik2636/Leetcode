class Solution:
    def countDigits(self, num: int) -> int:
        k=num
        count=0
        while num>0:
            d=num%10
            if (d!=0 and k%d==0):
                count+=1
            num//=10
        return count

        