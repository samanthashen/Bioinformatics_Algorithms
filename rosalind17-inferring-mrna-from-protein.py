aminonums = {'F':2, 'L':6, 'I':3, 'M':1, 'V':4, 'S':6,
 'P':4, 'T':4, 'A':4, 'Y':2, 'H':2, 'Q':2,
 'N':2, 'K':2, 'D':2, 'E':2, 'C':2, 'W':1,
 'R':6, 'G':4}

stop = 3

file = open('rosalind17test.txt', "r")
protein = ''.join(file.read().split())
file.close()

t_len = 0
for i in range(len(protein)):
    x = protein[i]
    if i == 0:
        t_len = aminonums[x]
    if i > 0:
        t_len = t_len * aminonums[x]

print("****")
print(t_len*stop)       

final = t_len*stop%1000000

print("FINAL********************")
print(final)

h = open("rosalind17ans.txt", "w+")
h.write(str(final))
h.close()
