k = 23
m = 17
n = 18

totalpop = k+m+n

probk = (k/totalpop)*((k-1)/(totalpop-1)) + (k/totalpop)*(m/(totalpop-1)) + (k/totalpop)*(n/(totalpop-1))
probm = 0.75*((m/totalpop)*((m-1)/(totalpop-1))) + (m/totalpop)*(k/(totalpop-1)) + 0.5*((m/totalpop)*(n/(totalpop-1)))
probn = 0*((n/totalpop)*((n-1)/(totalpop-1))) + (n/totalpop)*(k/(totalpop-1)) + 0.5*((n/totalpop)*(m/(totalpop-1)))

prob = str(probk+probm+probn)

print(prob)

h = open("rosalind7ans.txt", "w+")
h.write(prob)
h.close()
