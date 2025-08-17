class Solution:
    def findComplement(self, num: int) -> int:
        Bnum=bin(num)[2:]
        final=""
        for i in Bnum:
            if i =="1":
                final+="0"
            else:
                final+="1"
        return int(final,2)