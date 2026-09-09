class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # nums.sort()
        # return nums[n//2]

        # dict1={}
        # for i in range(n):
        #     if nums[i] not in dict1:
        #         dict1[nums[i]]=1
        #     else:
        #         dict1[nums[i]]+=1
        # for k,v in dict1.items():
        #     if v>n//2:
        #         return k

        candidate = None
        vote=0
        for i in range(len(nums)):
            if vote==0:
                candidate=nums[i]
                vote=1
            elif nums[i]==candidate:
                vote+=1
            else:
                vote-=1
        return candidate

        