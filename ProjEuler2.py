
two = [1,2]
fibsum = 0
sumOfEvens = 2 # to include first instance of 2

while fibsum < 4000000:
	fibsum = two[0] + two[1]
	if fibsum % 2 == 0:
		sumOfEvens += fibsum
	two.pop(0)
	two.append(fibsum)

print sumOfEvens
