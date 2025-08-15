class Solution:
    def reverseWords(self, s: str) -> str:
        final=""
        for i in s.split(" "):
            final=final+i[::-1]+" "
        return final[0:len(final)-1]