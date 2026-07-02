from Bio import SeqIO

seqdict = {}
file = open('rosalind5test.txt')
k = SeqIO.parse(file, 'fasta')
for fasta in k:
    seqdict[fasta.id] = str(fasta.seq)
file.close()

gccontent=0
gcdict = {}
for x in seqdict:
    print(x)
    for character in seqdict[x]:
        if character == "G":
            gccontent = gccontent + 1
        elif character == "C":
            gccontent = gccontent + 1
    gccontent = gccontent/len(seqdict[x])*100
    gcdict[x]=gccontent
    gccontent = 0

print(gcdict)

num = 0
highestcontent = ""
for x in gcdict:
    if gcdict[x] > num:
        highestcontent = x
        num = gcdict[x]

print(highestcontent)
print(num)

finalcommon = highestcontent + "\n" + str(num)

h = open("rosalind5ans.txt", "w+")
h.write(finalcommon)
h.close()

