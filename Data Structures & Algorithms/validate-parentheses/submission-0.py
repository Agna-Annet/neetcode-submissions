class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        def isEmpty():
            return len(stack)==0

        def push(s):
            stack.append(s)

        def pop():
            if isEmpty():
                return -1
            else:
                return stack.pop()
        
        for ch in s:
            if ch in ("(","{","["):
                push(ch)
            else:
                l=pop()
                if (ch==")" and l!="(") or (ch=="}" and l!="{") or (ch=="]" and l!="["):
                    return False
        if isEmpty()!=True:
            return False
        return True