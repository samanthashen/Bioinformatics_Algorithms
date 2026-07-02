from Bio import SeqIO

fasta_iterator = SeqIO.parse("rosalind18test.txt", "fasta")

for seq in fasta_iterator:
    print("id", seq.id)
    dnaseq = seq.seq

print(dnaseq)

if len(dnaseq)%3 == 1:
    dnaseq = dnaseq[:-1]
elif len(dnaseq)%3 == 2:
    dnaseq = dnaseq[:-2]

print(dnaseq)

def get_ambig_aa(codon_table,codon):
    aas = set()
    for n3 in 'ACGT':
        codon1 = codon[:2]+n3
        aas.add(codon_table[codon1])
    if len(aas) > 1:
        return 'x'
    return aas.pop().upper()

# Compute reverse complement
comp = dict(A='T',C='G',G='C',T='A')

def revComp(seq):
    rc = []
    for nuc in reversed(seq):
        rc.append(comp.get(nuc,nuc))
    rcseq = ''.join(rc)
    return rcseq

# Determine amino-acid translation based on codon table in "codons".
# Frame is assumed to be 1, 2, or 3. Any codon missing from the table
# are first checked to see if it has an N in the last position - if
# so, get_ambig_aa is called to see if all possible DNA symbols result
# in the same amino-acid. Any other type of codon missing from the
# codon table is translated as X. Add N's to end of sequence so that
# the last codon has three symbols in it.
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




# Call the appropriate functions to get the codon table and the sequence

seq = dnaseq


translations = []
for frame in (1,2,3):
    translations.append(trans(codons,seq,frame))
    
rcseq = revComp(seq)

for frame in (1,2,3):
    translations.append(trans(codons,rcseq,frame))

print(translations)

orfs = []
for frame in translations:
    for i in range(len(frame)):
        if frame[i] == "M":
            print(i)
            if frame[i:].find("*") != -1:
                stop = frame[i:].find("*") + i
                orfs.append(frame[i:stop])
            else:
                orfs.append(frame[i:])

s = set(orfs)

h = open("rosalind18ans.txt", "w+")
for x in s:
    h.write(x+"\n")
h.close()



'''

h = open("rosalind18ans.txt", "w+")
h.write(str(final))
h.close()
'''
