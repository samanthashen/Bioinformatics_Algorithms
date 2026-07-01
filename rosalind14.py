from Bio import SeqIO

seqs = []
file = open('rosalind14test.txt')
k = SeqIO.parse(file, 'fasta')
for fasta in k:
    seqs.append(str(fasta.seq))
file.close()

print(seqs)

commonmotifs = set()
for x in range(0,len(seqs)):
    for y in range(0, len(seqs)):
        if x!=y:
            print(seqs[x], seqs[y])
            for lenx in range(len(seqs[x])):
                #print(seqs[x][:lenx], seqs[x][lenx:])
                if seqs[x][:lenx] in seqs[y]:
                    print("if", seqs[x][:lenx])
                    commonmotifs.add(seqs[x][:lenx])
                elif seqs[x][lenx:] in seqs[y]:
                    print("elif", seqs[x][lenx:])
                    commonmotifs.add(seqs[x][lenx:])

print(commonmotifs)

mostcommon = {}
for common in commonmotifs:
    for seq in seqs:
        if common in seq:
            mostcommon[common]="yes"
        else:
            mostcommon[common]="no"
            break
print(mostcommon)

finalcommon = ""
greatestlen = 0
for x in mostcommon:
    if mostcommon[x]=="yes":
        print("x", x, mostcommon[x])
        if len(x)>greatestlen:
            finalcommon = x
            greatestlen = len(x)

print(finalcommon)


h = open("rosalind14ans.txt", "w+")
h.write(finalcommon)
h.close()
