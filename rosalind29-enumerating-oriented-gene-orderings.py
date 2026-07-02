from Bio import SeqIO

fasta_iterator = SeqIO.parse("rosalind29test.txt", "fasta")

seqlist = []
for seq in fasta_iterator:
    seqlist.append(str(seq.seq))

sequence = seqlist[0]
spliced = seqlist[1]

print("spliced", spliced)

positions = ""
count = 0
for nuc in spliced:
    position = sequence.find(nuc)
    positions = positions + str(position + 1 + count) + " "
    count = count + position + 1
    sequence = sequence[position + 1:]

print(seqlist, positions)


h = open("rosalind29ans.txt", "w+")
h.write(positions)
h.close()

