class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l_max=[0]*n
        r_max=[0]*n
        
        ans=0
        l_max[0]=height[0]
        r_max[n-1]=height[n-1]
        
        for i in range(1,n):
            l_max[i]=max(l_max[i-1],height[i])
        for j in range(n-2,-1,-1):
            r_max[j]=max(r_max[j+1],height[j])
        for i in range(n):
            ans+=min(l_max[i],r_max[i])-height[i]
        return ans

        