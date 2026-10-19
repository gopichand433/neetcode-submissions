class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for i in strs:
            res+=str(len(i))+'#'+i
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        j=1
        while i < len(s):
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            w=s[j+1:j+1+l]
            res.append(w)
            i=j+1+l
            j=i+1
        return res