class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        for i in operations:
            if i not in "+DC":
                lst.append(int(i))

            elif i == "D":
                p=lst[-1]*2
                lst.append(p)
            elif i=="+":
                lst.append(lst[-1]+lst[-2])
            else:
                lst.pop(-1)
        return sum(lst)