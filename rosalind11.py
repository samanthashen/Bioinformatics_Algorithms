n = 92
m = 16

a = []
c = []

for month in range(n):
    if month == 0:
        a.append(0)
        c.append(1)
    elif month < m:
        c.append(a[month-1])
        a.append(a[month-1]+c[month-1])
    elif month >=m:
        c.append(a[month-1])
        a.append(a[month-1]+c[month-1]-c[month-m])

print(a)
print(c)
print(a[n-1]+c[n-1])
outputstring = str(a[n-1]+c[n-1])

h = open("rosalind11ans.txt", "w+")
h.write(outputstring)
h.close()
