class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort=sorted(heights,reverse=True)
        final=[]
        for i in sort:
            ind=heights.index(i)
            final.append(names[ind])
        return final