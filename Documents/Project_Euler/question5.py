'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

def num_generator():
	i = 40
	while (not all_div(i)):
		i = i+1
	return i
def all_div(num):
	for i in xrange(1,21):
		if num%i == 0:
			continue
		else:
			return False
	return True


