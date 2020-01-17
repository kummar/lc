class Solution:
	# 两数之和
	# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	# Output: 7 -> 0 -> 8
	# Explanation: 342 + 465 = 807.
	def twoSum(self, nums, target):
		# 使用Map进行处理
		result = {}
		for i, v in enumerate(nums):
			remaining = target - v
			if remaining in result:
				return [result[remaining], i]
			result[v] = i
		return []

	# 双指针版本
	def twoSum2(self, numbers, target):
		left, right = 0, len(numbers) - 1
		while left < right:
			if numbers[left] + numbers[right] < target:
				left += 1
			if numbers[left] + numbers[right] > target:
				right -= 1
			if numbers[left] + numbers[right] == target:
				return [left + 1, right + 1]

	# 整数反转
	# Input 123  -123
	# Output 321 -321
	def reverse(self, x):
		if x == 0:
			return 0
		if x > 0:
			# 先将Int转化为Str，再使用List切片进行反转
			result = int(str(x)[::-1])
		else:
			result = -int(str(abs(x))[::-1])
		mina = -2 ** 31
		maxa = 2 ** 31 - 1
		if(result in range(mina, maxa)):
			return result
		else:
			return 0

	# 是否回文
	# Input  123
	# Output True
	def isPalindrome(self, x):
		if x >= 0:
			# 先将Int转化为Str，再使用List切片进行反转
			result = int(str(x)[::-1])
			if result == x:
				return True
			else:
				return False
		else:
			return False

	# 有效的括号
	# Input {}[]
	# Output True
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
					# 利用栈的特性进行判断
					top_element = stack.pop()
					if x != top_element:
						return False
					else:
						continue
				else:
					return False
		return len(stack) == 0

	# 去除重复数字
	# Given nums = [1,1,2] Return 2
	# Given nums = [0,0,1,1,1,2,2,3,3,4] Return 5
	def removeDuplicates(self, nums):
		if nums:
			slow = 0
			# 快慢指针
			for fast in range(1, len(nums)):
				if nums[fast] != nums[slow]:
					slow += 1
					nums[slow] = nums[fast]
			return slow + 1
		else:
			return 0

	# Merge 两个有序数组
	# Input:
	# nums1 = [1, 2, 3, 0, 0, 0], m = 3
	# nums2 = [2, 5, 6], n = 3
	# Output: [1, 2, 2, 3, 5, 6]
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		# two get pointers for nums1 and nums2
		# 双指针，从后往前
		p1 = m - 1
		p2 = n - 1
		# set pointer for nums1
		p = m + n - 1

		# while there are still elements to compare
		while p1 >= 0 and p2 >= 0:
			if nums1[p1] < nums2[p2]:
				nums1[p] = nums2[p2]
				p2 -= 1
			else:
				nums1[p] = nums1[p1]
				p1 -= 1
			p -= 1

		# add missing elements from nums2
		nums1[:p2 + 1] = nums2[:p2 + 1]

	# 股票最佳买卖时间
	"""
	Input: [7,1,5,3,6,4]
	Output: 5
	Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
				 Not 7-1 = 6, as selling price needs to be larger than buying price.
	Example 2:
	Input: [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transaction is done, i.e. max profit = 0.
	"""
	def maxProfit(self, prices):
		if not prices: return 0

		min_price = float('inf')
		max_profit = 0

		for price in prices:
			if price < min_price:
				min_price = price
			elif max_profit < price - min_price:
				max_profit = price - min_price
		return max_profit

	# 寻找不重复的数
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a = 0
		for i in nums:
			# 可以采用XOR进行计算
			# a ^ a = 0
			# a ^ 0 = a
			a ^= i
		return a