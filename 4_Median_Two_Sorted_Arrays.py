import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Sort the array
        merged_list = nums1 + nums2
        sorted_list = sorted(merged_list)        
        median_value = 0
        
        # Determine an odd or even number of numbers
        if len(sorted_list) % 2 != 0:
            print("odd")
            median_index = math.floor(len(sorted_list)/2)
            median_value = sorted_list[median_index]
        else:            
            lower_index = len(sorted_list)/2 - 1
            upper_index = len(sorted_list)/2
            median_value = (sorted_list[int(upper_index)] + sorted_list[int(lower_index)]) / 2            
        
        return median_value
