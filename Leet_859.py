class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        Hash1=Counter(s)
        Hash2=Counter(goal)
        if Hash1==Hash2 and s!=goal:
            count=0 
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    count+=1
            if count >2:
                return False
            else:
                return True
        elif Hash1 == Hash2 and s==goal:
            for i in Hash1.values():
                if i>=2:
                    return True
            return False
        else:
            return False