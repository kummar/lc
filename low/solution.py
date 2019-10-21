class Solution:
	def twoSum(self, nums, target):
		for i, value in enumerate(nums):
			if (target - value) in nums[i+1::]:
				return [i, nums.index(target - value)]
		return []

	def reverse(self, x):
		if x == 0:
			return 0
		if x > 0:
			print("S")

