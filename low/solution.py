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

	def addTwoNumbers(self, l1, l2):
		result = []
		result_tail = result
		carry = 0

		while l1 or l2 or carry:
			val1 = (l1.value if l1 else 0)
			val2 = (l2.value if l2 else 0)
			carry, out = divmod(val1 + val2 + carry, 10)

			result_tail.next = [out]
			result_tail = result_tail.next

			l1 = (l1.next if l1 else None)
			l2 = (l2.next if l2 else None)

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

		return result.next
