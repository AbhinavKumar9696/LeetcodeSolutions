class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[0:len(s)//2]
        b=s[len(s)//2:]
        count1=0
        count2=0
        for i in range(len(s)//2):
            if a[i]in "aeiouAEIOU":
                count1+=1
            if b[i]in "aeiouAEIOU":
                count2+=1
        if count1==count2:
            return True
        else:
            return False