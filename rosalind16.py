from Bio import SeqIO
import requests
import os.path
import urllib
file = open('rosalind16keys.txt', "r")
nums = file.read().split()
file.close()

IdList = []
for id in nums:
    IdList.append(id)

motif_dict = {}
for tempid in IdList:
    if len(id) > 6:
        id = tempid[:6]
    else:
        id = tempid
    url = "https://www.uniprot.org/uniprot/"+id+".fasta"
    response = urllib.request.urlopen(url)
    with open(id+".fasta", "b+w") as f:
        f.write(response.read())

    fasta_iterator = SeqIO.parse(id+".fasta", "fasta")

    for seq in fasta_iterator:
        seqlist = []
        for x in range(len(seq.seq)-2):
            if seq.seq[x] == "N":
                if seq.seq[x+1] != "P":
                    if seq.seq[x+2] == "S":
                        if seq.seq[x+3] != "P":
                            seqlist.append(str(x+1))                        
                    elif seq.seq[x+2] == "T":
                        if seq.seq[x+3] != "P":
                            seqlist.append(str(x+1))
        motif_dict[tempid] = seqlist
        seqlist = []
h = ""
i = 0
for x in motif_dict:
    i = i + 1
    h = h + x + "\n"+ " ".join(motif_dict[x])
    if i != len(IdList):
        h = h + "\n"

print(h)


t = open("rosalind16ans.txt", "w+")
t.write(h)
t.close()
