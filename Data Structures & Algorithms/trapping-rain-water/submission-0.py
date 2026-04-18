class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pref=[0]*n
        suff=[0]*n
        pref[0]=0
        suff[n-1]=0

        for i in range(1,n):
            pref[i]=max(pref[i-1],height[i-1])

        for i in range(n-2,-1,-1):
            suff[i]=max(suff[i+1],height[i+1])

        water=0
        for i in range(n):
            water+=max(0,min(pref[i],suff[i])-height[i])
        
        return water