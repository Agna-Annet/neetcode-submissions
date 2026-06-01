class Solution:
    def search(self, nums: List[int], target: int) -> int:        

        def bin_search(l,r,target):

            if l>r:
                return -1

            mid=(l+r)//2

            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                return bin_search(l,mid-1,target)
            else:
                return bin_search(mid+1,r,target)


        l,r=0,len(nums)-1

        if(len(nums)==1):
            return 0 if nums[0] == target else -1

        index=0

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        index=l
        
        left=bin_search(0,index-1,target)
        if left==-1:
            return bin_search(index,len(nums)-1,target)
        else:
            return left

        