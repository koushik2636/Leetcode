class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             prod*=nums[j]
        #             j+=1
        #     res.append(prod)
        # return res

        prefix=[1]*len(nums)
        sufix=[1]*len(nums)
        res=[1]*len(nums)
        prod=1
        
        for i in range(len(nums)):
            prefix[i]=prod
            prod=prod*nums[i]
        prod=1
        for i in range(len(nums)-1,-1,-1):
            sufix[i]=prod
            prod=prod*nums[i]

        for i in range(len(nums)):
            res[i]=prefix[i]*sufix[i]
        return res




        