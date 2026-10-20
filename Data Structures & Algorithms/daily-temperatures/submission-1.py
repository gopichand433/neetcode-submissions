class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        res=[0]*len(temp)
        st=[]
        for i,t in enumerate(temp):
            while  st and t>st[-1][1]:
                sti,stt=st.pop()
                res[sti]=(i-sti)
            st.append([i,t])
        return res
