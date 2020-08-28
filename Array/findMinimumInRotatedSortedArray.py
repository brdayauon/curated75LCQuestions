class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:  #only one in the num array
            return nums[0]
        
        #binarySearch
        left = 0
        right = len(nums) - 1
        
        if nums[0] < nums[right]:  #there is no pivot (rotation)
            return nums[0]
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            
            
            