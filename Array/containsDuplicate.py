class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
                
        for i,key in freq.items():
            if key > 1:
                return True
            
        return False