import math


def isCur(n):
    t = 0
    for i in str(n):
        if i == 0:
            return False

        t += math.factorial(int(i))

        if t > n:
            return False

    if n == t:
        return True
    return False


winner = 0
for i in range(10, 9999):
    if isCur(i):
        print("Success: {}".format(i))
        winner = i


print(winner)
