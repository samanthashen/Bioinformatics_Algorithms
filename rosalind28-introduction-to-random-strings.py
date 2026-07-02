import math

file = open('rosalind28test.txt', "r")
characters = file.read().split()
file.close()

print(characters)

seq = characters[0]
gc_array = map(float, characters[1:])

at_count = seq.count("A") + seq.count("T")
gc_count = seq.count("C") + seq.count("G")

print(gc_count, at_count)

print(seq)
new_array = []
for x in gc_array:
    gc_prob = gc_count * math.log10(x/2)
    at_prob = at_count * math.log10((1-x)/2)
    prob = gc_prob + at_prob
    new_array.append(str(round(prob, 3)))

joined = " ".join(new_array)

print(joined)

h = open("rosalind28ans.txt", "w+")
h.write(joined)
h.close()
