from itertools import permutations
from math import factorial

n = 7

perms = factorial(n)

num = permutations(range(1, n+1))

h = open("rosalind19ans.txt", "w+")
h.write(str(perms)+"\n")
for x in num:
    h.write(' '.join(map(str,x)) + "\n")
h.close()
