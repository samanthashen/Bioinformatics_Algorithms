from Bio import SeqIO

seqs = {}
file = open('rosalind12test.txt')
k = SeqIO.parse(file, 'fasta')
for fasta in k:
    seqs[fasta.id] = (str(fasta.seq)[:3], str(fasta.seq)[-3:])
file.close()

edges = []
for x in seqs:
#    print(x, seqs[x], seqs[x][0], seqs[x][1])
    for y in seqs:
        if x!=y:
#            print(x, seqs[x][1], y, seqs[y][0])
            if seqs[x][1]==seqs[y][0]:
                edges.append((x,y))

outputstring = ""
for pair in range(len(edges)):
    if pair == (len(edges)-1):
        outputstring = outputstring + edges[pair][0]+" "+edges[pair][1]
    else:
        outputstring = outputstring + edges[pair][0]+" "+edges[pair][1]+"\n"

print(outputstring)

h = open("rosalind12ans.txt", "w+")
h.write(outputstring)
h.close()
