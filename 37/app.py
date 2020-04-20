import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_tr(n):
    s = str(n)
    s1 = list(s)
    s2 = list(reversed(s1))

    if not is_prime(n):
        return False

    if len(s) < 2:
        return False

    for i in range(1, len(s)):
        x = int(s[i:])
        y = int(s[:i])

        if not is_prime(x) or not is_prime(y):
            return False

    return True


winner = 0
c = 0
count = 0
result_list = []
while c < 11:
    count += 1

    if is_tr(count):
        c += 1
        winner = count
        result_list.append(count)

print("result_list:")
print(result_list)
print("sum:")
print(sum(result_list))
