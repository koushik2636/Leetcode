class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in candies:
            count=0
            val=i+extraCandies
            for j in candies:
                if val>=j:
                    count+=1
            if count==len(candies):
                l.append(True)
            else:
                l.append(False)
        return l
    
        