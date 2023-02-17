
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        high = len(nums) - 1
        low = 0
       
        while low <= high:
            pointer = (low+high) // 2
            if nums[pointer] < target:
                #ignore bottom half
                low = pointer +1
            elif nums[pointer] > target:
                high = pointer - 1
            else:
                return pointer
        return -1
