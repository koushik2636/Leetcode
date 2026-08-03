class Solution:
    def toLowerCase(self, s: str) -> str:
        v=""
        for i in range(len(s)):
            if s[i].isupper():
                v=s[i].lower()
                s=s.replace(s[i],v)

        return s
