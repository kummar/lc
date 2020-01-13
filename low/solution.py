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

	def isPalindrome(self, x):
		if x >= 0:
			result = int(str(x)[::-1])
			if result == x:
				return True
			else:
				return False
		else:
			return False

	def isValid(self, s):
		stack = []
		map = {
			"{": "}",
			"[": "]",
			"(": ")"
		}
		for x in s:
			if x in map:
				stack.append(map[x])
			else:
				if len(stack) != 0:
					top_element = stack.pop()
					if x != top_element:
						return False
					else:
						continue
				else:
					return False
		return len(stack) == 0

	def removeDuplicates(self, nums):
		if nums:
			slow = 0
			for fast in range(1, len(nums)):
				if nums[fast] != nums[slow]:
					slow += 1
					nums[slow] = nums[fast]
			return slow + 1
		else:
			return 0