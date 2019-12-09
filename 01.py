# 233168
sum_so_far = 0

for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		sum_so_far += i

print(sum_so_far)