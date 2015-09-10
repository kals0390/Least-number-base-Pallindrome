import math
def check_prime(n):
	if n == 1 or n == 2 or n ==3:
		return True
	else:
		sq_num = int(math.sqrt(n)) 
		for i in xrange(2,(sq_num+1)):
			if n %i  == 0:
				return False
		return True				

	
def main(number):
	
	
	factor_limit = int(math.sqrt(number))
	largest = find_factors(number,factor_limit)

	print "largest factor is ",largest

def find_factors(num,list):
	largest = 0
	for factor in xrange(2,list):
		if num % factor == 0:
			if check_prime (factor):
				largest = factor
	return largest


