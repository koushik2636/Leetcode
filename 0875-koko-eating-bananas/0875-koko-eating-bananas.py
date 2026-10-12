class Solution:
    def calculate_time(self,piles,b_count):
        time=0
        for i in range(len(piles)):
            time+=math.ceil(piles[i]/b_count)
        return time

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            time=self.calculate_time(piles,mid)
            if time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


        