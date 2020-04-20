import itertools

numbers = "".join([str(i) for i in range(10)])


def isPandigital(n):
    for num in numbers:
        if num not in n:
            return False

    for i in range(1, len(n)-2):
        sub = int(n[i:(i+3)])

        if i == 1 and sub % 2 != 0:
            return False
        if i == 2 and sub % 3 != 0:
            return False
        if i == 3 and sub % 5 != 0:
            return False
        if i == 4 and sub % 7 != 0:
            return False
        if i == 5 and sub % 11 != 0:
            return False
        if i == 6 and sub % 13 != 0:
            return False
        if i == 7 and sub % 17 != 0:
            return False

    return True


nums = [str(i) for i in range(10)]

winner = 0
for ls in itertools.permutations(nums):
    gl = "".join([str(it) for it in list(ls)])
    if isPandigital(gl):
        winner += int(gl)

print(winner)
