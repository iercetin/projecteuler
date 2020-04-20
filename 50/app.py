import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


limit = 1000000

primes = []
c = 1
while sum(primes) < limit:
    c += 1
    if is_prime(c):
        primes.append(c)


l = primes

total = 0
winner = []

for x in range(len(l)):
    for y in range(x, len(l)):
        gls = l[x:y+1]

        if not len(gls) > 1:
            continue

        s = sum(gls)

        if s > limit:
            continue

        if is_prime(s) and len(gls) > total:
            total = len(gls)
            winner = gls


# print(winner)
print(sum(winner))
