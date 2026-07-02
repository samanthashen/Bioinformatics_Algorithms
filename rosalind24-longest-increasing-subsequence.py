file = open('rosalind24test.txt', "r")
characters = file.read().split()
file.close()

firstnum = int(characters[0])
othernums = list(map(int, characters[1:]))

print(firstnum, othernums[0])

def sequence(othernums, sort_type):
    leno = [1] * len(othernums)
    for x in range(len(othernums)):
        for y in range(x+1, len(othernums)):
            if sort_type == "increasing":
                if othernums[x] < othernums[y]:
                    leno[y] = max(leno[y],leno[x]+1)
            if sort_type == "decreasing":
                if othernums[x] > othernums[y]:
                    leno[y] = max(leno[y],leno[x]+1)
                    
    final_list = []
    big = max(leno)
    for i in range(len(othernums)-1,-1,-1):
        if big==leno[i]:
            final_list.append(othernums[i])
            big = big-1
    return(final_list[::-1])

inc_list = sequence(othernums, "increasing")
dec_list = sequence(othernums, "decreasing")

text_put = ""
for i in inc_list:
    text_put = text_put + str(i) + " "

text_put = text_put + "\n"

for i in dec_list:
    text_put = text_put + str(i) + " "

h = open("rosalind24ans.txt", "w+")
h.write(text_put)
h.close()
