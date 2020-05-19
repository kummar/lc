l1 = [2, 4, 3]
l2 = [1, 1, 4]

# Get Length
len_l1 = len(l1)
len_l2 = len(l2)

carry = 0
answer = []
if len_l1 >= len_l2:
	for i in range(0, len(l1)):
		temp = l1[i] + l2[i] + carry
		print(temp)
		if temp >= 10:
			result = 10 - temp + temp % 10
			print(result)
			answer.append(result)
			carry += 1
		else:
			answer.append(temp)

print(answer)