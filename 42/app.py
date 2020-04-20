import string
letters = list(string.ascii_lowercase)


def nthTriangle(n):
    return int(n * (n+1) / 2)


triangles = [nthTriangle(i) for i in range(1, 100)]


def wordVal(word):
    v = 0
    for w in word.lower():
        v += letters.index(w) + 1
    return v


f = open("p042_words.txt").read()
words = list(f.split(","))
words = [w.replace("\"", "") for w in words]


winner = 0
for word in words:
    wordValue = wordVal(word)
    if wordValue in triangles:
        print("YES: Word: {}, Value: {}".format(word, str(wordValue)))
        winner += 1

print("Result: {}".format(str(winner)))
