from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        Hash=Counter(s)
        count=0
        if len(s)<k:
            return False
        elif len(s)==k:
            return True
        else:
            for i in Hash.values():
                if i%2==1:
                    count=count+1
            
            if count<=k:
                return True
            else:
                return False