import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        
        return nums[int(math.ceil(len(nums)/2))-1] if len(nums)%2 == 1 else (nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2