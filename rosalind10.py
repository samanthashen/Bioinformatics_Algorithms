from Bio import SeqIO

seqs = []
file = open('rosalind10test.txt')
k = SeqIO.parse(file, 'fasta')
for fasta in k:
    seqs.append(str(fasta.seq).upper())
file.close()

seqlen = len(seqs[0])

a, t, c, g = (0, 0, 0, 0)
rows, cols = (4, seqlen)
profile = [[0 for i in range(cols)] for j in range(rows)]

sortlist = []
consensus = []
for i in range(seqlen):
    for seq in seqs:
        if seq[i]=="A":
            a = a + 1
        elif seq[i] == "T":
            t = t + 1
        elif seq[i] == "C":
            c = c + 1
        elif seq[i] == "G":
            g = g + 1
    profile[0][i]=a
    profile[1][i]=c
    profile[2][i]=g
    profile[3][i]=t
    if a>=c and a>=g and a>=t:
        consensus.append("A")
    elif c>=a and c>=g and c>=t:
        consensus.append("C")
    elif t>=c and t>=g and t>=a:
        consensus.append("T")
    else:
        consensus.append("G")
                
    a, t, c, g = (0, 0, 0, 0)

pstring = "A: " + (' '.join(map(str, profile[0]))) + "\nC: " + (' '.join(map(str, profile[1]))) + "\nG: " + (' '.join(map(str, profile[2]))) + "\nT: " + (' '.join(map(str, profile[3])))


cstring=""
for x in consensus:
    cstring = cstring + x
print(cstring + "\n" + pstring)

h = open("rosalind10ans.txt", "w+")
h.write(cstring + "\n" + pstring)
h.close()
