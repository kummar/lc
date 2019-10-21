class Solution:
	def twoSum(self, nums, target):
		result = {}
		for i, v in enumerate(nums):
			remaining = target - v
			if remaining in result:
				return [result[remaining], i]
			result[v] = i
		return []

	def reverse(self, x):
		if x == 0:
			return 0
		if x > 0:
			print("S")

