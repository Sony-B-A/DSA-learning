# Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
    
        for key in hash_map:
            if key == x:
                return hash_map[key]
        return 0