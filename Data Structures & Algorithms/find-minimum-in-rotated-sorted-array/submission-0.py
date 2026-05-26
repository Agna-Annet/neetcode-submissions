class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        if(len(nums)==1):
            return nums[0]

        while(True):
            mid=(l+r)//2

            if(nums[0]<=nums[mid] and nums[mid+1]<=nums[-1]):
                return min(nums[0],nums[mid+1])
            
            elif nums[0]>nums[mid]:
                r=mid
            elif nums[mid+1]>nums[-1]:
                l=mid+1