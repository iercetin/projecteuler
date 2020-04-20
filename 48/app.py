t = 0
for i in range(1, 1001):
    t += i ** i

winner = t % 10**10

print(winner)
