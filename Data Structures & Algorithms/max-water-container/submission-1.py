class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mp=0
        p=0
        l=0
        h=len(heights)-1
        while l<h:
            w=h-l
            hi=min(heights[l],heights[h])
            p=w*hi
            if p>mp:
                mp=p
            if heights[l] > heights[h]:
                h-=1
            else:
                l+=1
        return mp
        