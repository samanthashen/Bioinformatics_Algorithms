#n = 36
#k = 2

n = 32
k = 5


gen1 = 1
gen2 = 0
gen3 = 0
for x in range(n):
    gen1 = gen1+gen3
    gen3 = gen2
    gen2 = gen1*k
    print(gen1, gen2, gen3)
    
print(gen1)

h = open("rosalind4ans.txt", "w+")
h.write(str(gen1))
h.close()
