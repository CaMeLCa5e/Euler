#! /usr/bin/python 

r = range(1,1000)
count = 0
for number in r:
	#take out all numbers divisable by 3 or 5.
	if number % 3 == 0 or number % 5 == 0:
		count += number
print count


