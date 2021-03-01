class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # need to use two pinter technique
        
        i = 0   #our slower pointer
        j = 0   #our faster pointer
        
        for j in range(len(nums)): #iterate through the list with j
            if nums[j] != nums[i]:  #if number at j does not equal to the number at i (so if next number over is unique)
                i += 1              # then we move the i pointer over to the next unique number
                nums[i] = nums[j]   # makes sense when done visually, basically we are moving and if i and j are different, we want j to become i so that we are shortening the length in place. draw it out and walk through if you get confused again
        return i + 1            # if num at j doesnt equal the one at i we do nothing bc theyre unique
        
        
        
        '''
        #print(nums)
        length = len(List)
        for i in range(length):
            if nums[]
            print(nums)
            
        we need two pointers, one to keep track of unique elements and one to get length of new array
        delete the replicated numbers in the array and 
         length = len(List)
        for i in range(List):
            if nums[i] == nums[i+1]:
                List.remove(nums[i+1])
                length = length - 1
            #else:
        print(List)
        
          nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
        
        TIME COMPLEXITY: O(N) because we only go through the list once.

        '''


            
