from math import factorial

file = open('rosalind27test.txt', "r")
characters = file.read().split()
file.close()

n = int(characters[0])
k = int(characters[1])

ans = int((factorial(n)/factorial(n-k)) % 1000000)


h = open("rosalind27ans.txt", "w+")
h.write(str(ans))
h.close()

