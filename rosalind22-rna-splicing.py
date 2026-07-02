from Bio import SeqIO

def get_ambig_aa(codon_table,codon):
    aas = set()
    for n3 in 'ACGT':
        codon1 = codon[:2]+n3
        aas.add(codon_table[codon1])
    if len(aas) > 1:
        return 'x'
    return aas.pop().upper()

def trans(codons,seq,frame):
    seq += 'N'*(frame-1)
    aalist = []
    for i in range(frame-1,len(seq),3):
        codon = seq[i:i+3]
        if codon in codons: 
            aa = codons[codon]
        elif codon.count('N') == 1 and codon[2] =='N':
            aa = get_ambig_aa(codons,codon)
        else:
            aa = 'X'
        aalist.append(aa)
    aaseq = ''.join(aalist)
    return aaseq

h = open("codontable.txt", "r")
data = {}
for l in h:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value
h.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')


fasta_sequences = SeqIO.parse(open('rosalind22test.txt'),'fasta')
i=0
seq = ''
introns = []
for fasta in fasta_sequences:
    if i == 0:
        seq = str(fasta.seq)
    else:
        introns.append(str(fasta.seq))
    i = i+1

print(seq)
print(introns)
#print(seq.find(introns[0]))
#startpos = seq.find(introns[0])
#print(seq[:startpos]+seq[startpos+len(introns[0]):])

startpos = 0
for intron in introns:
    startpos = seq.find(intron)
    seq = seq[:startpos] + seq[startpos+len(intron):]

print(seq)

print(trans(codons, seq, 1))

ans = trans(codons, seq, 1)

print(ans[:-1])

h = open("rosalind22ans.txt", "w+")
h.write(ans[:-1])
h.close()
