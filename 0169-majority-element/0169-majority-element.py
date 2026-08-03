class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checked=[]
        
        for i in range(len(nums)):
            if nums[i] not in checked:
                checked.append(nums[i])
                if nums.count(nums[i])> len(nums)/2:
                    return nums[i]
        