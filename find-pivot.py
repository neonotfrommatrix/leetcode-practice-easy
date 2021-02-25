"""
ARRAYS AND STRINGS SECTION


Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

EXAMPLE: 
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11


Reminder for Natalie: the sumR and sumL will update each iteration!
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumL = 0
        sumR = sum(nums)
        
        for i in range(len(nums)):
            sumL = sumL + nums[i]
            
            if sumL == sumR:
                return i
            sumR = sumR - nums[i]
            
        return -1
