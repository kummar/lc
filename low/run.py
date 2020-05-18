l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1_in = l1[::-1]
l2_in = l2[::-1]

result_1 = 0
for i in range(0, len(l1_in)):
	print(l1_in[i])
	result_1 += 10 ** (len(l1_in) - i - 1) * l1_in[i]
	print(result_1)
result_2 = 0
for i in range(0, len(l2_in)):
	print(l2_in[i])
	result_2 += 10 ** (len(l2_in) - i - 1) * l2_in[i]
	print(result_2)
result = result_1 + result_2
answer = []
for i in str(result):
	answer.append(int(i))
print(answer)
