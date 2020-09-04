class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0 
        curr = 0 
        
        for i in range(0,len(nums)):
            temp = curr
            curr = max(nums[i]+prev, curr)
            prev = temp
            
        #want to return curr
        return curr