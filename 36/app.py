def decimal_to_bin(n):
    return "{0:b}".format(n)


def is_valid_number(n):
    return len(str(int(n))) == len(n)


def is_pal(s):
    if not is_valid_number(s):
        return False

    m = int(len(s)/2)
    for i in range(m):
        a = s[i]
        b = s[len(s)-i-1]
        if a != b:
            return False
    return True


b = decimal_to_bin(585)

winner = 0
for j in range(1, 1000000):
    if is_pal(str(j)) and is_pal(str(decimal_to_bin(j))):
        #print("j: {}".format(j))
        winner += j

print(winner)
