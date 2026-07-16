class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        left=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        for i in range(len(nums)):
            s=abs(left-(sum-nums[i]-left))
            res.append(s)
            left+=nums[i]
        return res

        