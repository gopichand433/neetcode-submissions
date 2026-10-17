class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r={}
        for i in nums:
            r[i]=r.get(i,0)+1
        
        sorted_items = sorted(r.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]