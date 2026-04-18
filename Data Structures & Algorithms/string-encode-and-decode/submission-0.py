class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            num=len(i)
            s+=str(num)+'#'+i
        return s

    def decode(self, s: str) -> List[str]:
        L=[]
        i=0
        while i<len(s):
            num=''
            while s[i]!='#':
                num+=s[i]
                i+=1
            num=int(num)
            j=i+1
            i=i+num+1 
            L.append(s[j:i])       
        return L


