class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for val in nums:
            for d in str(val):
                l.append(int(d))
        return l
        