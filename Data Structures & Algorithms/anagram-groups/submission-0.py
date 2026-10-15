class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=defaultdict(list)
        for i in strs:
            c=[0]*26
            for x in i:
                c[ord(x)-ord("a")]+=1
            s[tuple(c)].append(i)
        return list(s.values())