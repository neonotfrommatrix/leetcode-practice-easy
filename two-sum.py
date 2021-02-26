"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].


"""





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        target - x = someNum
        
        scan list for that number:
        
        if it is in that list, return x index and the someNum index
        """
        #edge case
        if len(nums)<= 0:
            return False
        
        # create an empty dictionary
        dict1 = {}
        
        # for loop through the list
        for i in range(len(nums)):
        
        # if not it equals target then return that statement
            if nums[i] in dict1:
                return dict1[nums[i]], i 
        
        # if num is not in the dictionary, place it inside the dict
            else:
                targetPair = target - nums[i]
                dict1[targetPair] = i
    
    """
ok so this one is a bit confusing - because i was not completely familiar with dictionarys. 
    
    at fist the dictionary is empty
    dict = {} 
    
    iterate through the list
    for in range len(nums)
    
    if the number is in this dictionary then return that and the index
    
    else (if not in the dict, then we place the specialNum and i in dict)
    specialNum = target - num[i]
    dict[specialNum] = i
    
    
    
    
    
    
    
    
    
    
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


so for exaple [3,2,4] with target=6

lets iterate through the list

i=0
nums[i]=3
specialNum = 6 - 3 = 3

then we dict[specialNum] =i

dict = {3 : 0}

ok now go thru the loop again

i=1
nuims[i]=2
specialNum = 6 - 2 = 4

check if nums[i], in this case 2, is in dict={3:0}
nope so skip this if

else
specialNum is 4
dict[4] = i

so now our dict is {3:0, 4:1}


OK now for through for loop so we are at 
i = 2
nums[i]=4
specialNum = 6 - 4 = 2

check if 4 is  in dict={3:0, 4,1}
YES IT IS RIGHT THERE

return the index 1 from {4,1} and the i  we are on (2)
so that should return [1,2]
        
    
    
    """
