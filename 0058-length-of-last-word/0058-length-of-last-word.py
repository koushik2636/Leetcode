class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        length=0
        for i in range(len(s)-1,-1,-1):
            if ord(s[i])!=32:
                length+=1
            elif ord(s[i])==32:
                break
        return length
            
        