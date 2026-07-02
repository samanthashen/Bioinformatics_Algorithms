file = open('rosalind20test.txt', "r")
protein = file.read().strip()
file.close()

wt = {}
file = open('mass.txt', "r")
for line in file:
    row = line.split()
    print(row)
    wt[row[0]] = float(row[1])
file.close()

print(protein)
print(wt)

total_wt = 0
for amino in protein:
    total_wt = total_wt + wt[amino]

print(total_wt)

h = open("rosalind20ans.txt", "w+")
h.write(str(total_wt))
h.close()
