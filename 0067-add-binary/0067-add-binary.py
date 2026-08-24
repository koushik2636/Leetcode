class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a)
        y=int(b)
        res1=0
        res2=0
        i=0
        j=0
        while x>0:
    
            d=x%10
            res1+=d*(2**i)
            x//=10
            i+=1

        while y>0:
    
            d=y%10
            res2+=d*(2**j)
            y//=10
            j+=1

        bi=bin(res1+res2)
        str1=str(bi)
        return str1[2:]
        


        