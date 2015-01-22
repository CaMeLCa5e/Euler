# scratchpad.py


r = range(1,1000)
count = 0
for number in r:
	if number % 3 == 0 or number % 5 == 0:
		count += number
print count


print sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0])












