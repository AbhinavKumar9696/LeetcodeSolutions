class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            count=0
            for i in str(num):
                count=count+int(i)
            num=count
        return num