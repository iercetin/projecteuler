import math
import itertools


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


nums = [str(i) for i in range(1, 10)]

winner = 0
for x in range(2, 10):
    nums = [str(i) for i in range(1, x)]

    for ls in itertools.permutations(nums):
        ls = int("".join([str(it) for it in list(ls)]))
        if is_prime(ls) and ls > winner:
            winner = ls

print(winner)
