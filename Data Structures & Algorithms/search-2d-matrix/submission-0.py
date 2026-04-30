class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the required row
        low=0
        high=len(matrix)-1

        while low<=high:
            row=(low+high)//2

            if target>matrix[row][-1]:
                low=row+1
            elif target<matrix[row][0]:
                high=row-1
            else:
                break

        else:
            return False

        low=0
        high=len(matrix[row])-1
        row=matrix[row]
        while low<=high:
            mid=(low+high)//2

            if target==row[mid]:
                return True
            elif target<row[mid]:
                high=mid-1
            else:
                low=mid+1
        return False