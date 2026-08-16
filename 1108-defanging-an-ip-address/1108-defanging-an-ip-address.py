class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.','[.]')

        ans=''
        for i in address:
            if i not in '.':
                ans+=i
            else:
                ans+='[.]'
        return ans        