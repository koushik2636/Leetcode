class Solution:
    def isPalindrome(self, s: str) -> bool:
        # for i in s:
        #     if not (65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57):
        #         s=s.replace(i,"")
               
        # s=s.lower()
        # if s==s[::-1]:
        #     return True
        # else:
        #     return False

                
        #two pointer

        s=s.lower()
        i=0
        j=len(s)-1

        while i<j:

            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        