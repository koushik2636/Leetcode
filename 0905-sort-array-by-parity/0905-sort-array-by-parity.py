class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        odd=[]
        if n<=1:
            return nums
        k=0
        for i in nums:
            if i%2==0:
                nums[k]=i
                k+=1
            else:
                odd.append(i)
        nums[k:]=odd
        return nums

        