import timeit

def tuya(word1, word2):
    wordn1 = list(word1)
    for i, valor in enumerate(word2):
        wordn1.insert(i * 2 + 1, valor)
    return "".join(wordn1)

def mia(word1, word2):
    n = min(len(word1), len(word2))
    return "".join(map("".join, zip(word1, word2))) + word1[n:] + word2[n:]

a, b = "abcdefghij" * 10, "pqrstuvwxy" * 10
print(timeit.timeit(lambda: tuya(a, b), number=100000))
print(timeit.timeit(lambda: mia(a, b), number=100000))

