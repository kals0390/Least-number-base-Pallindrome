def check_pallindrome(num):
	num_list =[]
	rev_list = []
	i = num
	while i!= 0:

		rev_list.append(i%10)
		i = i/10
	num_list = rev_list[::-1]

	if num_list == rev_list:
		return True
	else:
		return False

def main():
	largest = 0
	for i in xrange(100,1000):
		for j in xrange(100,1000):
			num = i*j
			if check_pallindrome(num):
				if num>largest:
					largest = num
					digit_1 = i
					digit_2 = j

	print "largest number is  and ", largest,digit_1,digit_2





