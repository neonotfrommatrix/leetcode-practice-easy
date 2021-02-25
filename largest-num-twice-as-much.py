"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.


Ex. 
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)

        if all(m >= 2*x for x in nums if x != m):
            # arrayname.index(maxValue) is valid
            return nums.index(m)
        return -1
         

#all function returns True if all items in an iterable are true, otherwise it returns False.

#If the iterable object is empty, the all() function also returns True.

#number_list = [1, 2, 3]
#max_value = max(number_list)
#Return the max value of the list


#max_index = number_list.index(max_value)
#Find the index of the max value


#print(max_index)
