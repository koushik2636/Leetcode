class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l=[]
        str1 = "".join(map(str, digits))
        int1=int(str1)+1
        str2=str(int1)
        for i in str2:
            l.append(int(i))
        return l

        