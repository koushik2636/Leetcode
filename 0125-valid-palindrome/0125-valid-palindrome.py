class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not (65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57):
                s=s.replace(i,"")
               
        s=s.lower()
        if s==s[::-1]:
            return True
        else:
            return False

                

        