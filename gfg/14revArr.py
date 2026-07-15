# Given an array arr, you need to reverse a subarray of that array.
# The range of this subarray is given by indices l and r (1-based indexing).

# lavel: basic

class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		l-=1
		r-=1
		while l<r:
		    arr[l], arr[r] = arr[r], arr[l]
		    l, r = l+1, r-1
		return arr