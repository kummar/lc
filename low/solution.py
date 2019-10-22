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
			result = int(str(x)[::-1])
		else:
			result = -int(str(abs(x))[::-1])
		mina = -2 ** 31
		maxa = 2 ** 31 - 1
		if(result in range(mina, maxa)):
			return result
		else:
			return 0

