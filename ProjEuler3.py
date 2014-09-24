

# there's nothing here...

'''import math

num = 600851475143
factorList = []

sqrt = math.sqrt(num) + 1

for i in range(1, int(sqrt)):
	if num % i == 0:
		factorList.append(i)

factorList2 = []

for i in factorList:
	factorList2.append(num / i)
factorList += factorList2

for
print factorList'''


# this solution is found here: http://zacharydenton.com/project-euler-solutions/3/
# comments are mine and his

import math

def factorize(n):
    res = []
    # iterate over all even numbers first. keep adding them to the array, until you can't divide by 2 any more
    while n % 2 == 0:
        res.append(2)
        n //= 2

    # try odd numbers up to sqrt(n) - n is new, however.
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res
#600851475143
print max(factorize(600851475144))


