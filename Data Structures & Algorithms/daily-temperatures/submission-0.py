class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*n
       
        for i in range(n):
            temp=temperatures[i]
            while stack and stack[-1][1]<temp:
                last=stack.pop()
                result[last[0]]=i-last[0]
            stack.append((i,temp))
                
        return result