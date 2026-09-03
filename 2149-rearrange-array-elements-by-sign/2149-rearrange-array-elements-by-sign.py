class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        z=0
        for j in range(len(p)):
            nums[z]=p[j]
            z+=2
        r=1
        for k in range(len(n)):
            nums[r]=n[k]
            r+=2
        return nums


        
        