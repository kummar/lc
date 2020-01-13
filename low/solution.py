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

	def isVaild(self, s:str) -> bool:
		stack = []
		c_map = {
			"{" : "}",
			"[" : "]",
			"(" : "}"
		}
		for x in s:
			if x in map:
				stack.append(c_map[x])
			else:
				if (len(stack) != 0):
					top_element = stack.pop()
					if x != top_element:
						return False
					else:
						continue
				else:
					return False

			return len(stack) == 0