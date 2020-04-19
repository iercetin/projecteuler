import math
import itertools

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def new_list(ls):
	nl 	= []
	for i in range(1,len(ls)):
		nl.append(ls[i])
	nl.append(ls[0])
	return nl

def rotated_lists(l):
	rl = [l]
	for i in range(len(l)-1):
		nl = new_list(rl[i])
		rl.append(nl)
	return rl


def is_circular_prime(n):
	l 	= list(str(n))
	rl 	= rotated_lists(l)

	for el in rl:
		num = int("".join([str(e) for e in el]))
		if not is_prime(num):
			return False
	return True

count = 0
for i in range(2,1000000):
	if is_circular_prime(i):
		print(i)
		count += 1

print("C: {}".format(count))
