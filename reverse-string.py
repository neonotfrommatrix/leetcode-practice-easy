"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        """
        thinking. two pointer. ok one fast and one slow pointer? we need to modify in place. so im thinking we switch. We take the first char of the string and switch it with the last char of the string. but how do we do it simulatneously. unless we add it to theback and push everything further? we create a temp variable !
        
        1st attempt; didn't work lol
        
        i = 0
        j = (len(s)-1)
        for i in range(len(s)):
            temp = s[i]
            s[i] == j[i]
            j[i] == temp
        return s
            
        O(N) time bc bigger array more time
        O(1) space because doing it  in place
        """
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left] = s[right]
            s[right] = s[left]
            
            left = right+1
            right = left-1
        
        """
        we set the first index to left side of string and the right side to last index.
        while they are on opposite sides of the string, we swap
        then move our pointers over
        """
        
        
