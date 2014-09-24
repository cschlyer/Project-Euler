
import time

start = time.time()

bigVal = 0

for i in range(100, 1000):
	for j in range(i,1000): # use i to avoid duplicates
		mult = i*j
		if mult > bigVal and str(mult) == (str(mult)[::-1]):
			bigVal = mult

elapsed = (time.time() - start)

print 'The largest palindrome is ', bigVal
print elapsed

# 0.194329977036 - time without avoiding duplicates
# 0.110751867294 - time avoiding duplicates