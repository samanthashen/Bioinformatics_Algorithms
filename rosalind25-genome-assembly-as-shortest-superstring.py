from Bio import SeqIO

fasta_iterator = SeqIO.parse("rosalind25test.txt", "fasta")

seqlist = []
for seq in fasta_iterator:
    seqlist.append(str(seq.seq))

print(seqlist)
print(len(seqlist))

finalstr = ""
for x in range(len(seqlist)):
    print(x)
    try:
        seq = seqlist[x]
    except IndexError:
        break
    seql = len(seq)
    if seql%2==0:
        half = int(seql/2-1)
    else:
        half = int((seql-1)/2)
    seqlist.pop(x)
    for y in range(len(seqlist)):
        try:
            if seqlist[y].endswith(seq):
                seqlist.pop(y)
                finalstr = finalstr + seq[half:]
            else:
                seqlist.pop(y)
                finalstr = seq[:half] + finalstr
        except IndexError:
            break
print(finalstr)

h = open("rosalind25ans.txt", "w+")
h.write(finalstr)
h.close()

