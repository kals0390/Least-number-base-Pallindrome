'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def is_prime(n):
	if n == 1 or n == 2 or n ==3:
		return True
	else:
		sq_num = int(math.sqrt(n)) 
		for i in xrange(2,(sq_num+1)):
			if n %i  == 0:
				return False
		return True

def prime_count():
	i=0
	num =1 
	while i <= 10001:
	
		if is_prime(num):
			i +=1
		num+=1
	return num-1


