class Solution:
    def maximum69Number (self, num: int) -> int:
        output=""
        count=0
        for i in str(num):
            if i=="9":
                output=output+"9"
            elif i!="9"and count<1:
                output=output+"9"
                count=count+1
            else:
                output=output+i
        
        return int(output)