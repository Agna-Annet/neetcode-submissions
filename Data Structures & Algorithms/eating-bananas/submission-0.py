class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)

        Min=high

        while low<=high:
            mid=(low+high)//2

            time=[ math.ceil(i/mid) for i in piles]
            time=sum(time)
            if time<=h:
                Min=mid
                high=mid-1
            else:
                low=mid+1
        
        return Min