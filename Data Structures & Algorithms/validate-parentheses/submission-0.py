class Solution:
    def isValid(self, s: str) -> bool:
        m={ ")" : "(", "]" : "[", "}" : "{" }
        stack=[]
        for i in s:
            if i in m:
                if stack and stack[-1]==m[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
        