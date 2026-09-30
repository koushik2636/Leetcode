class Solution:
    def searchRange(self, arr: list[int], target: int) -> list[int]:
        l1=0
        h1=len(arr)-1
        f=-1
        while l1<=h1:
            mid=(l1+h1)//2
            if arr[mid]==target:
                h1=mid-1
                f=mid
            elif arr[mid]<target:
                l1=mid+1
            else:
                h1=mid-1
        l2=0
        h2=len(arr)-1
        l=-1
        while l2<=h2:
            mid=(l2+h2)//2
            if arr[mid]==target:
                l=mid
                l2=mid+1
            elif arr[mid]<target:
                l2=mid+1
            else:
                h2=mid-1
        return [f,l]
