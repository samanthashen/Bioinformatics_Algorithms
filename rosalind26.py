from Bio import SeqIO
from math import factorial

fasta_iterator = SeqIO.parse("rosalind26test.txt", "fasta")

seq = ""
for seq in fasta_iterator:
    seq = str(seq.seq)

ucount = seq.count("U")
gcount = seq.count("G")

matches = factorial(ucount) * factorial(gcount)

h = open("rosalind26ans.txt", "w+")
h.write(str(matches))
h.close()

