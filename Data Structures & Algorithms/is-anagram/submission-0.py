class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        Ds={}
        Dt={}
        for i in range(len(s)):
            Ds[s[i]]=1+Ds.get(s[i],0)
            Dt[t[i]]=1+Dt.get(t[i],0)
        return Ds==Dt