# 4613732
fib = [1, 1]
fibsum = 0

for i in range(1, 11):
	newfib = fib[i] + fib[i - 1]	
	if newfib < 4000000:
		fib.append(newfib)
		if newfib % 2 == 0:
			fibsum = fibsum + newfib
	else:
		break
# print(fib)
print(fibsum)

# =====================
# fibsum = 0
# a, b = 1, 1

# while a < 4000000:
# 	(a, b) = (b, a + b)
# 	if a % 2 == 0:
# 		fibsum += a

# print(fibsum)
# =====================