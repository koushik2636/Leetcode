class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        for i in range(k):
            w+=nums[i]
        s=w
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            s=max(w,s)
        return s/k