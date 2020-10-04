class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = []
        for idx_x, x in enumerate(nums):
    
            for y in range(idx_x+1,len(nums)):
                test_val = x + nums[y]
                if test_val == target:
                    index = [idx_x,y]
                    break
            if test_val == target:
                break
        return index
