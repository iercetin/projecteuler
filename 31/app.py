import itertools

l = [1,2,5,10,20,50,100,200]
x = [0,200]

c = itertools.combinations(l,1)

used = []
for i in range(1,200):
	c = itertools.combinations(l,i)

	for cm in c:
		print(cm)

		s = sum(list(cm))
		if s == 200:
			if not cm in used:
				used.append(cm)

print(used)
print(len(used))